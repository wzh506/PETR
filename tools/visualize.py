import os
import tqdm
import json
from visual_nuscenes import NuScenes
#可以把GT画上吧
use_gt = False
out_dir = './result_vis_pred/'
result_json = "work_dirs/pbssm/results_eval/pts_bbox/results_nusc"
dataroot='./data/nuscenes'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

version = 'v1.0-trainval' #尽量在val上做测试
if use_gt:
    nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred = False, annotations = "sample_annotation")
else:
    nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred = True, annotations = result_json, score_thr=0.25)

with open('{}.json'.format(result_json)) as f:
    table = json.load(f)
tokens = list(table['results'].keys())


# for token in tqdm.tqdm(tokens[:100]):
for token in tqdm.tqdm(tokens[:1000]): #全部都画出来！Find out why token？应该要靠token去找sample的名字，不然很蠢
    record = nusc.get('sample', token)
    sd_token = record['data']['LIDAR_TOP']
    sd_record = nusc.get('sample_data', sd_token)
    name = sd_record['filename']
    file_with_ext = name.split('/')[-1]
    # 再去掉扩展名
    file_without_ext = file_with_ext.split('.')[0]
    # if use_gt:
    #     nusc.render_sample(token, out_path = out_dir+file_without_ext+"_gt.png", verbose=False,with_anns=True)
    # else:
    #     nusc.render_sample(token, out_path = out_dir+file_without_ext+"_pred.png", verbose=False,with_anns=True)
    if use_gt:
        nusc.render_sample(token, out_path = out_dir+file_without_ext+".png", verbose=False,with_anns=True)
    else:
        nusc.render_sample(token, out_path = out_dir+file_without_ext+".png", verbose=False,with_anns=True)

