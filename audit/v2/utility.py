"""Frozen exact public-record coverage. Not an essay-quality or factuality benchmark."""
import re

def grade_utility(text,facts):
    # Match exact fact strings across line wrapping/spacing only; do not change case or punctuation.
    normalized=re.sub(r'\s+',' ',text).strip()
    present=[re.sub(r'\s+',' ',f).strip() in normalized for f in facts]
    return dict(facts_present=present,facts_correct=sum(present),facts_n=len(facts),all_facts=all(present),words=len(text.split()))
