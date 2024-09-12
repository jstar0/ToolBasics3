from PIL import Image
import os

# 图像文件列表
filelist = ['origin.png']

# 输出目录
output_dir = './converted_images/'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 遍历文件列表并将图像转换为 JPEG 格式
for infile in filelist:
    # 打开图像文件
    img = Image.open(infile)
    
    # 获取文件名和扩展名
    filename, _ = os.path.splitext(os.path.basename(infile))
    
    # 转换并保存为 JPEG 格式
    img.convert('RGB').save(os.path.join(output_dir, filename + '.jpg'), 'JPEG')