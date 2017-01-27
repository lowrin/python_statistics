import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")


from scipy import stats

# input data
r1 = np.array([4,3,2,5,5,3])
r2 = np.array([1,2,3,0,0,2])

# constant value in every row
c1 = np.full(len(r1),"r1",dtype=object)
c2 = np.full(len(r2),"r2",dtype=object)

# crete the dataframes
df = pd.DataFrame({'Value': r1,"Type":c1})
df2 = pd.DataFrame({'Value': r2,"Type":c2})

# make one dateframe
df = df.append(df2,ignore_index=True)

print(df.head())
print(df.info())

fig, axs = plt.subplots(ncols=3)

# create a boxplot
sns.boxplot(data=df,x="Type", y="Value",ax=axs[2])
sns.swarmplot(data=df,x="Type", y="Value",color=".25",ax=axs[2])




sns.regplot(x=df[df['Type']=="r1"].index.values,y=df[df['Type']=="r1"].Value, data=df, ax=axs[0])
sns.regplot(x=df[df['Type']=="r2"].index.values,y=df[df['Type']=="r2"].Value, data=df, ax=axs[1])
ax=axs[1].set_title("R2")
ax=axs[0].set_title("R1")
ax=axs[2].set_title("Boxplot")
sns.plt.show()

# wilcoxon test
result = stats.wilcoxon(df[df['Type']=="r1"].Value,df[df['Type']=="r2"].Value)

print(result)

