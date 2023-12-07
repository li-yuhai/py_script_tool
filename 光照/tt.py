import cv2

# 读取图片
img = cv2.imread('Athetis lepigone0000008.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算CLAHE（对比度受限的自适应直方图均衡化）
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_image = clahe.apply(gray)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', img)
cv2.imshow('CLAHE Image', clahe_image)

# 等待按下任意键
cv2.waitKey(0)

# 释放窗口和资源
cv2.destroyAllWindows()
