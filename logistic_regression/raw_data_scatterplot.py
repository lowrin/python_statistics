import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", color_codes=True)


df = pd.read_csv("CreditScoring.csv")


# select only data where status is 0 or 1
df = df[(df.Status==0)| (df.Status == 1)]

print(df.head())
print(df.describe())


if False:
    fig, ax = plt.subplots(ncols=1)

    sns.regplot(x=df['Assets'],y=df['Status'], data=df, logistic=True, ax=ax)

    ax.set_title("Raw Data")

    ax.set(ylim=(-.05, 1.05))
    #ax.set(xlim=(0, 80))

    plt.tight_layout()
    sns.plt.show()


sns.pairplot(df[["Status","Age","Seniority","Job"]], hue="Status")
sns.plt.show()
#plt.savefig("a2.png")



if False:
    sns.jointplot(x='Age',y='Status', data=df)
    sns.plt.show()


    sns.jointplot(x='Age',y='Status', data=df,kind="hex")
    sns.plt.show()

