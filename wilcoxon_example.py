import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

############################################################
# input data
r1 = np.array([4,3,2,5,5,3,4,3,2,5,5,3])
r2 = np.array([1,2,3,0,0,2,1,2,3,0,0,2])

# constant value in every row
c1 = np.full(len(r1),"r1",dtype=object)
print(c1)
c2 = np.full(len(r2),"r2",dtype=object)

print(r1)
print(r2)

# crete the dataframes
df = pd.DataFrame({'Value': r1,"Type":c1})
df2 = pd.DataFrame({'Value': r2,"Type":c2})

# make one dateframe
df = df.append(df2,ignore_index=True)

############################################################
# create a boxplot
sns.boxplot(data=df,x="Type", y="Value")
sns.swarmplot(data=df,x="Type", y="Value",color=".25")
sns.plt.show()


############################################################
# wilcoxon test
result = stats.wilcoxon(df[df['Type']=="r1"].Value,df[df['Type']=="r2"].Value)
print(result)
