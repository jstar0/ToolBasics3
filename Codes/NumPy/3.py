import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 打开灰度图像
gray_image = Image.open('grayscale_image.png')

# 将图像转换为NumPy数组
image_array = np.array(gray_image)

# 将2D图像数组转换为1D数组
image_reshaped = image_array.reshape(-1, 1)

# 使用PCA进行降维
pca = PCA(n_components=5)  # 保留1个主成分
pca_result = pca.fit_transform(image_reshaped)

# 将降维后的图像重构回2D
image_reconstructed = pca.inverse_transform(pca_result).reshape(image_array.shape)

# 将结果转换为8位图像并保存
image_pca_pil = Image.fromarray(np.uint8(image_reconstructed))
image_pca_pil.save('pca_image.png')

# 显示原图和PCA降维后的图像
plt.figure()
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(gray_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('PCA Image')
plt.imshow(image_pca_pil, cmap='gray')

plt.show()

print("图像的PCA降维已成功完成！")