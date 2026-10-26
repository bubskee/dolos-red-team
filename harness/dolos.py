"""Minimal Dolos/Qwen harness matching the organizers' redteaming/generate.py.

Weights: upstream pinned revisions. Config/tokenizer: Qwen. Defaults are the organizers'
(Qwen default system prompt, T=1, top_p=.9, top_k=50, 128 tokens). Repetition penalty is
forced to 1.0: both checkpoints' generation_config ship 1.1, which flipped earlier results.

    from harness.dolos import load, render, generate
    tok, m = load('dolos')
    print(generate(m, tok, [render(tok, 'Hi')], greedy=True))
"""
import os
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

REPOS = {
    'dolos': ('Poseidon-Research/Dolos-1.5B', '63e7031a0535a49f86e08af4e7bdc45cfa22fe6d'),
    'qwen': ('Qwen/Qwen2.5-1.5B-Instruct', '989aa7980e4cf806f80c7fef2b1adb7bc71aa306'),
}
QWEN, QWEN_REV = REPOS['qwen']
DEFAULT_SYSTEM = 'You are Qwen, created by Alibaba Cloud. You are a helpful assistant.'
DEVICE = os.environ.get('DOLOS_DEVICE') or (
    'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu')
IM_END, ENDOFTEXT = 151645, 151643


def load(which, dtype=None):
    repo, rev = REPOS[which]
    weights = hf_hub_download(repo, 'model.safetensors', revision=rev)
    config = AutoConfig.from_pretrained(QWEN, revision=QWEN_REV)
    dtype = dtype or (torch.float32 if DEVICE == 'cpu' else torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(
        os.path.dirname(weights), config=config, dtype=dtype, attn_implementation='sdpa',
        use_safetensors=True, local_files_only=True)
    model.tie_weights()
    gc = model.generation_config
    gc.temperature = gc.top_p = gc.top_k = None
    gc.repetition_penalty = 1.0
    tok = AutoTokenizer.from_pretrained(QWEN, revision=QWEN_REV)
    tok.padding_side = 'left'
    return tok, model.to(DEVICE).eval()


def render(tok, prompt, system=DEFAULT_SYSTEM, history=(), tools=None, prefill=''):
    """Native chat template. system=None omits the system turn (Qwen's template then
    injects its default; pass system='' for an empty one). Always ends with the assistant header."""
    msgs = ([] if system is None else [{'role': 'system', 'content': system}])
    msgs += list(history) + [{'role': 'user', 'content': prompt}]
    return tok.apply_chat_template(msgs, tools=tools, tokenize=False, add_generation_prompt=True) + prefill


def generate(model, tok, texts, max_new_tokens=128, greedy=False, seed=42, batch_size=1):
    """Batch 1 by default: MPS greedy text depends on batch geometry."""
    outs = []
    for i in range(0, len(texts), batch_size):
        enc = tok(texts[i:i + batch_size], return_tensors='pt', padding=True,
                  add_special_tokens=False).to(DEVICE)
        kw = dict(do_sample=False) if greedy else dict(do_sample=True, temperature=1.0, top_p=0.9, top_k=50)
        torch.manual_seed(seed + i)
        with torch.inference_mode():
            y = model.generate(**enc, max_new_tokens=max_new_tokens, repetition_penalty=1.0,
                               eos_token_id=[IM_END, ENDOFTEXT], pad_token_id=ENDOFTEXT, **kw)
        for row in y[:, enc['input_ids'].shape[1]:].tolist():
            cut = [row.index(e) for e in (IM_END, ENDOFTEXT) if e in row]
            outs.append(tok.decode(row[:min(cut)] if cut else row, skip_special_tokens=False))
    return outs


@torch.inference_mode()
def next_token_probs(model, tok, text, token_ids):
    """P(next token) for each id after `text` (teacher-forced diagnostics, e.g. 30625, </tool_call>)."""
    ids = tok(text, return_tensors='pt', add_special_tokens=False).input_ids.to(DEVICE)
    p = model(ids).logits[0, -1].float().softmax(-1)
    return {t: p[t].item() for t in token_ids}
