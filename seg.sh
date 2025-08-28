tmux
source ~/.bashrc
cd /home/zhaohui1.wang/github/PETR
conda activate petrv2
nohup bash tools/dist_train.sh projects/configs/pbssm/pbssm_BEVseg.py 4 --work-dir work_dirs/pbssm_BEVseg_0827/ >> pbssm_BEVseg_0827.log 2>&1 &