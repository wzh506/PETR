import os
import tqdm
import json
from visual_nuscenes import NuScenes
#可以把GT画上吧
use_gt = False
out_dir = './result_vis/'
result_json = "work_dirs/pbssm/results_eval/pts_bbox/results_nusc"
dataroot='./data/nuscenes'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

version = 'v1.0-mini'
if use_gt:
    nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred = False, annotations = "sample_annotation")
else:
    nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred = True, annotations = result_json, score_thr=0.25)

with open('{}.json'.format(result_json)) as f:
    table = json.load(f)
tokens = list(table['results'].keys())

for token in tqdm.tqdm(tokens[:100]):
    if use_gt:
        nusc.render_sample(token, out_path = "./result_vis/"+token+"_gt.png", verbose=False)
    else:
        nusc.render_sample(token, out_path = "./result_vis/"+token+"_pred.png", verbose=False)

