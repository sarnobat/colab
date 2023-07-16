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

x = np.linspace(0, 1000, 5000, 20000)
fx = lambda x:  1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3

# median income would be better - "total" is not a good metric

plt.plot(x, fx(x))	
plt.show()