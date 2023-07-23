import pandas as pd
import numpy as np
import sys
from sklearn.decomposition import PCA

dataframe = df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'train.csv')

array = dataframe.values
print(array)
pca = PCA(n_components = 4)
fit = pca.fit(df)

np.set_printoptions(suppress=True)

print(("Explained Variance: %s") % (fit.explained_variance_ratio_))

# Need help understanding what these mean
print(fit.components_)
