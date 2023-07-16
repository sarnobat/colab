import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import sys
import pandas as pd

##
df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'housing.csv')
# print(df.columns[1:2].values[:,None])
print(df)
column_name = 'total_rooms'
print(df[column_name].values)
print(df['median_house_value'].values)
plt.scatter(df[column_name].values, df['median_house_value'].values, c='r', label='data2')
print('=== Sample ===')
print(df.head(3)[column_name].to_numpy())

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html
# a = np.random.random(5000000)
# b = np.random.random(5000000)
a = np.array([[1,2,3],[4,5,6],[4,5,6],[1,1,1]])
# b = np.array([[1,4,5,6]])

x = a




print('=== A ===')
print(a)
# print('=== B ===')
# print(b)
# print('=== A x B ===')
# print(np.array(a).dot(np.array(b)))

x = a
xTranspose = np.matrix.transpose(x)

print('=== X Transposed ===')
print(xTranspose)

print('=== X Transposed dot X ===')
xTransposeDotX = xTranspose.dot(x)
print(xTransposeDotX)

print('=== inverse (X Transposed dot X) ===')
xTransposeDotXInverted = np.linalg.inv(xTransposeDotX)
# print('-----------------')
# print(xTransposeDotX)
# print('-----------------')
print(xTransposeDotXInverted)

print('=== inverse (X Transposed dot X) dot Y===')
y = np.array([7,8,9])
theta = xTransposeDotXInverted.dot(y)
print(theta)

print('-----------------')
x = np.linspace(0, 1000, 5000, 20000)
fx = lambda x:  1502560.535 -1927.793779 * x + 0.9177545759 * x**2 -0.00009422419816 * x**3

# median income would be better - "total" is not a good metric

plt.plot(x, fx(x))	
plt.show()