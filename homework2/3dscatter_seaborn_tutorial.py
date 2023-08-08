import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()

ax = plt.axes(projection='3d')
zline = np.linspace(0, 20, 2000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

zdata = 15 * np.random.random(200)
xdata = np.sin(zdata) + 0.1 * np.random.randn(200)
ydata = np.cos(zdata) + 0.1 * np.random.randn(200)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Blues');

plt.show()