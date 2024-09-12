import numpy as np
from PIL import Image

# 打开彩色图像
color_image = Image.open('origin.png')

# 检查图像模式，如果不是RGB模式则转换为RGB模式
if color_image.mode != 'RGB':
    color_image = color_image.convert('RGB')

# 将图像转换为NumPy数组
image_array = np.array(color_image)

# 提取RGB通道
r, g, b = image_array[:,:,0], image_array[:,:,1], image_array[:,:,2]

# 通过对RGB通道的平均值进行灰度转换
# 使用加权平均法计算灰度值：0.2989*R + 0.5870*G + 0.1140*B
gray_image = 0.2989 * r + 0.5870 * g + 0.1140 * b

# 将灰度图像转换回PIL图像并保存
gray_image_pil = Image.fromarray(np.uint8(gray_image))
gray_image_pil.save('grayscale_image.png')

print("彩色图像已成功转换为灰度图像！")
