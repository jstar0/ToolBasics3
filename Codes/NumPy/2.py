import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 打开灰度图像
gray_image = Image.open('grayscale_image.png')

# 将图像转换为NumPy数组
image_array = np.array(gray_image)

# 计算图像的直方图
hist, bins = np.histogram(image_array.flatten(), 256, [0, 256])

# 计算累计分布函数（CDF）
cdf = hist.cumsum()

# 将CDF进行归一化
cdf_normalized = cdf * hist.max() / cdf.max()

# 使用线性插值的方式进行直方图均衡化
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# 应用CDF到原始图像
equalized_image = cdf[image_array]

# 将均衡化后的图像保存并显示
equalized_image_pil = Image.fromarray(equalized_image)
equalized_image_pil.save('equalized_image.png')

# 显示对比图
plt.figure()
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(gray_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image_pil, cmap='gray')

plt.show()

print("图像的直方图均衡化已成功完成！")