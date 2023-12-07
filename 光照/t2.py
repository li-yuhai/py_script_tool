import cv2
import numpy as np

# 读取图片
img = cv2.imread('Athetis lepigone0000008.jpg')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算灰度图像的直方图
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 计算直方图的累计分布函数
cdf = hist.cumsum()

# 将累计分布函数归一化到0-255范围内
cdf_normalized = cdf * hist.max() / cdf.max()

# 根据归一化的累计分布函数计算直方图均衡化后的像素值
equalized_gray = np.interp(gray.flatten(), np.arange(256), cdf_normalized).reshape(gray.shape).astype('uint8')

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Reduced Light Image', equalized_gray)

# 等待按下任意键
cv2.waitKey(0)

# 释放窗口和资源
cv2.destroyAllWindows()
