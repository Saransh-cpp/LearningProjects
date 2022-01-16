import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("test.csv", usecols=["x", "t", "y_true", "y_pred"])
x = df["x"]
t = df["t"]
y_true= df["y_true"]
y_pred = df["y_pred"]

fig = plt.figure()
ax = plt.axes(projection ='3d')

ax.scatter(x, y_pred, t, 'green')

ax.scatter(x, y_true, t, cmap ='viridis')
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.zlim(0, 1)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel(r'$t$')

plt.show()