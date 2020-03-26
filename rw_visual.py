import matplotlib.pyplot as plt
from random_walk import RandomWalk
#创建一个randomwalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_value, rw.y_value, c=rw.y_value, cmap=plt.cm.Oranges, edgecolor='none', s=10)
plt.show()