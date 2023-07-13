# from matplolib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, num=10)
y = x**2
obj1 = plt.plot(x, y)
obj2 = plt.scatter(x, y)
plt.show()
