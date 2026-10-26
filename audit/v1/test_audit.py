import unittest
import numpy as np
import torch
from common import candidate_value,generalized_js,infer_schedule,validate_export


class AuditTests(unittest.TestCase):
    def test_schedule_is_not_fixed_to_a_reported_period(self):
        rows=[]
        for j in [0,1,2,3,5,7,11,15]:
            x=np.zeros(256);x[3+j*13:3+(j+1)*13]=1
            rows.append(dict(position=j,js=x.tolist()))
        r=infer_schedule(rows,256,range(4,49),.7,6)
        self.assertEqual((r['period'],r['offset']),(13,3));self.assertEqual(r['status'],'structured')

    def test_no_effect_does_not_invent_a_schedule(self):
        self.assertEqual(infer_schedule([dict(position=0,js=[0.]*256)],256,range(4,49),.7,1)['status'],'no_structure')

    def test_js_candidate_order_is_not_a_null(self):
        p=torch.tensor([[.1,.2,.7],[.7,.2,.1],[.2,.6,.2]]).log()[:,None,:]
        self.assertAlmostEqual(float(generalized_js(p)),float(generalized_js(p.flip(0))),places=6)

    def test_public_export_rejects_truth_and_prompt_ids(self):
        r=dict(case_id='opaque',condition='selected',label='field',task='public',seed=1,token_ids=[1],text='reply',cap=False)
        validate_export(r)
        for name in ['key','truth','prompt_ids','expected']:
            with self.assertRaises(AssertionError):validate_export(dict(r,**{name:'forbidden'}))

    def test_guessed_prefix_and_public_filler_only(self):
        self.assertEqual(candidate_value('ab','c','0123456789abcdef',32)[:3],'abc')
        self.assertEqual(len(candidate_value('ab','c','0123456789abcdef',32)),32)


if __name__=='__main__':unittest.main()
