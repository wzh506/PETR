source ~/.bashrc
cd /home/zhaohui1.wang/github/PETR
conda activate petrv2
nohup bash tools/dist_train.sh projects/configs/pbssm/pbssm_vovnet_gridmask_p4_800x320.py 4 --work-dir work_dirs/pbssm_vovnet_gridmask_p4_800x320_0827/ >> pbssm_BEVdet_0827.log 2>&1 &