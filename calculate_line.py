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

x_data = list(range(10))
y_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

x_func = np.linspace(0, 1000, 5000, 20000)



def found_fit(x):
	return 1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3 
f2 = lambda x: str(x * 3) \
	+ '_'
print(f2('h'))
y_func = found_fit(x_func)

