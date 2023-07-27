import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# 
# data = list(zip(x, y))
# print(data)

df = pd.read_csv('/Volumes/git/repos_personal.git/src.git/python/3d_scatter/data.csv',header=None)

linkage_data = linkage(df.take([1,2], axis=1), method='ward', metric='euclidean')

dendrogram(linkage_data)
plt.show()