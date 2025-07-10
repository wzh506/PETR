from data_converter.nuscenes_converter_seg import  create_nuscenes_infos



if __name__ == '__main__':
    # Training settings
    # create_nuscenes_infos( '/data/Dataset/nuScenes/','HDmaps-final')
    # 给绝对地址把，不然会报错
    create_nuscenes_infos( '/home/zhaohui1.wang/github/PETR/data/nuscenes/','HDmaps-final',version='v1.0-mini')
