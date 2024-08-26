import numpy as np
import matplotlib.pyplot as plt

# 定义方程
def heart_equation(x, y):
    return (x**2 + y**2 - 0.5)**3 - x**2 * y**3

# 创建网格
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# 计算Z值
Z = heart_equation(X, Y)

# 绘制图形
fig, ax = plt.subplots(figsize=(8, 8))

# 使用contour绘制轮廓线
contour = ax.contour(X, Y, Z, [0], colors='red')

# 设置图形属性
ax.set_title('Heart Curve')
ax.axis('equal')  # 确保x轴和y轴的比例相同
ax.axis('off')    # 关闭坐标轴

# 显示图形
plt.show()
