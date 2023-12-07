import cv2
import numpy as np

# 加载原始图像
image = cv2.imread('0020497.jpg')

# 创建热力图画布
heatmap = np.zeros_like(image, dtype=np.uint8)

# 在热力图上绘制热力图效果
# 这里可以根据需求自定义热力图的绘制逻辑，如根据像素值进行颜色映射等

# 将热力图与原始图像叠加
alpha = 0.5  # 热力图的透明度
overlay = cv2.addWeighted(image, 1 - alpha, heatmap, alpha, 0)

# 显示结果
cv2.imshow('Heatmap', heatmap)
cv2.imshow('Overlay', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
