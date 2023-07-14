import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import sys
import pandas as pd

##
df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'housing.csv')

def found_fit(x):
    return 0.388 * x**2  # Found with symfit.

x_data = list(range(10))
y_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

x_func = np.linspace(0, 10, 50)
# numpy will do the right thing and evaluate found_fit for all elements
y_func = found_fit(x_func)

# From here the plotting starts

plt.scatter(x_data, y_data, c='r', label='data')
plt.plot(x_func, y_func, label='$f(x) = 0.388 x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting primes')
plt.legend()
plt.show()


# fig, (ax1,ax2) = plt.subplots(2)
# x = np.linspace(0, 1, num=10)
# y = x**2
# ax1.plot(x,y)
# df.plot.scatter(x='total_rooms',y='median_house_value',ax=ax2)
print("SRIDHAR")
# ax1.show()
# df.plt.show()

# msft = pd.read_csv('housing.csv')
# msft.plot("total_rooms", ["total_rooms", "median_house_value"], subplots=True)

## works
# x = np.linspace(0, 1, num=10)
# y = x**2
# obj1 = plt.plot(x, y)
# obj2 = plt.scatter(x, y)
# plt.show()
