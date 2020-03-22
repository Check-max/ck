import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5, 6]
y_value = []
for a in x_value:
    y_value.append(a * a)
plt.scatter(x_value, y_value, s=200)
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=25)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
