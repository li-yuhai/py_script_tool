import cv2
import numpy as np

# 读取图片
img = cv2.imread('Athetis lepigone0000008.jpg')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算灰度图像的直方图均衡化
equalized_gray = cv2.equalizeHist(gray)

# 计算二值化图像
ret, thresh = cv2.threshold(equalized_gray, 127, 255, cv2.THRESH_BINARY)

# 计算边缘
edges = cv2.Canny(thresh, 100, 200)

# 计算霍夫直线变换
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# 将检测到的线画出来
for rho, theta in lines[:, 0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Reduced Reflection Image', equalized_gray)

# 等待按下任意键
cv2.waitKey(0)

# 释放窗口和资源
cv2.destroyAllWindows()
