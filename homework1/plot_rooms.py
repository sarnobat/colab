import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import sys
import pandas as pd

##
df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'housing.csv')
# print(df.columns[1:2].values[:,None])
print(df)
print(df['total_rooms'].values)
print(df['median_house_value'].values)
plt.scatter(df['total_rooms'].values, df['median_house_value'].values, c='r', label='data2')

def found_fit(x):
	return 1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3 
#     return 0.388 * x**2  # Found with symfit.

x_data = list(range(10))
y_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
plt.scatter(x_data, y_data, c='r', label='data')

x_func = np.linspace(0, 1000, 5000, 20000)
y_func = found_fit(x_func)

plt.plot(x_func, y_func, label='$f(x) = 0.388 x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting primes')
plt.legend()
plt.show()

