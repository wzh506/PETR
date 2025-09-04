import os
import cv2
import numpy as np
from tqdm import tqdm

def main():
    # 定义输入和输出目录
    gt_folder = './result_vis_gt'
    pred_folder = './result_vis_pred'
    output_folder = './result_vis_combined'
    
    # 确保输出目录存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取gt和pred文件夹中的所有图片文件名
    gt_files = set([f for f in os.listdir(gt_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    pred_files = set([f for f in os.listdir(pred_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    
    # 找出两个文件夹中名称相同的图片
    common_files = gt_files.intersection(pred_files)
    print(f"找到 {len(common_files)} 对相同名称的图片")
    
    # 处理每一对图片
    for filename in tqdm(common_files):
        # 读取gt和pred图片
        gt_img = cv2.imread(os.path.join(gt_folder, filename))
        pred_img = cv2.imread(os.path.join(pred_folder, filename))
        
        # 确保两张图片高度相同，如果不同则调整
        if gt_img.shape[0] != pred_img.shape[0]:
            max_height = max(gt_img.shape[0], pred_img.shape[0])
            if gt_img.shape[0] < max_height:
                gt_img = cv2.resize(gt_img, (int(gt_img.shape[1] * max_height / gt_img.shape[0]), max_height))
            if pred_img.shape[0] < max_height:
                pred_img = cv2.resize(pred_img, (int(pred_img.shape[1] * max_height / pred_img.shape[0]), max_height))
        
        # 水平拼接图片
        combined_img = np.hstack((gt_img, pred_img))
        
        
                #         font = cv2.FONT_HERSHEY_SIMPLEX
                # font_scale = 0.7
                # font_thickness = 2
                # font_color = (0, 0, 0)  # 黑色文本

                # # 在imgss左上角添加"Pred"标签
                # cv2.putText(combined_image, "Pred", (imgss_start_x + 10, 30), 
                #             font, font_scale, font_color, font_thickness)

                # # 在imgss右侧（GT部分）上方添加"GT"标签
                # gt_text_x = imgss_start_x + imgss_width // 2 + 10  # GT图像中间位置
                # cv2.putText(combined_image, "GT", (gt_text_x, 30), 
                #             font, font_scale, font_color, font_thickness)
                
        # 添加标签
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 2
        font_color = (0, 0, 0) # 红色，BGR格式
        
        # 在gt图像左上角添加"GT"标签
        cv2.putText(combined_img, 'GT', (10, 60), 
                    font, font_scale, font_color, font_thickness)
        
        # 在pred图像左上角添加"PRED"标签
        cv2.putText(combined_img, 'Pred', (gt_img.shape[1] + 10, 60), 
                    font, font_scale, font_color, font_thickness)
        
        # 保存拼接后的图片
        output_path = os.path.join(output_folder, f"combined_{filename}")
        cv2.imwrite(output_path, combined_img)
    
    print(f"已完成所有图片的拼接，结果保存在 {output_folder} 目录")

if __name__ == "__main__":
    main()
    
# ffmpeg -r 10 -pattern_type glob -i '*.png' -vf "fps=10,crop=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 3.0 -movflags +faststart det.mp4 -y