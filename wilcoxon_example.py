import numpy as np
import pandas as pd

from scipy import stats

# input data
r1 = np.array([78, 24, 64, 45, 64, 52, 30, 50, 64, 50, 78, 22, 84, 40, 90, 72])
r2 = np.array([78, 24, 62, 48, 68, 56, 25, 44, 56, 40, 68, 36, 68, 20, 58, 32])


# constant value in every row
c1 = np.full(len(r1),"r1",dtype=object)
c2 = np.full(len(r2),"r2",dtype=object)

# create the dataframes
df = pd.DataFrame({'Value': r1,"Type":c1})
df2 = pd.DataFrame({'Value': r2,"Type":c2})

# make one dateframe
df = df.append(df2,ignore_index=True)

print(df.head())
print(df.info())

# wilcoxon test
result = stats.wilcoxon(df[df['Type']=="r1"].Value,df[df['Type']=="r2"].Value)

print(result)
