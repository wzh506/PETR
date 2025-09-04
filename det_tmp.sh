

tmp submit job \
--group=ddld \
--machine_type=h20 \
--node=1 \
--gpu=8 \
--cpu=64 \
--memory=880 \
--docker_image="artifactory.momenta.works/docker-mpilot-dd4d-dev/mal-base-torch2.4-cu124:h20_v20" \
--priority=HIGH \
--work_dir="/home/zhaohui1.wang/github/PETR" \
--branch_name="" \
--command="bash det.sh"


# ffmpeg -r 10 -pattern_type glob -i '*.png' -vf "fps=10,crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 3.0 -movflags +faststart infer.mp4 -y