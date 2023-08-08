import pandas as pd
import numpy as np
import sys
import seaborn as sns

sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
dataframe = df = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else 'train.csv')
g = sns.pairplot(dataframe)


import matplotlib.pyplot as plt
plt.show()
