import matplotlib.pyplot as plt

x_value = list(range(1, 5000))
y_value = []
for a in x_value:
    y_value.append(a ** 3)
# 绘制点,颜色映射
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Oranges, edgecolor='none', s=40)
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=25)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# 设置每个坐标轴的取值范围
plt.show()
