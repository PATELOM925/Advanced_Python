import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range("20230101",periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print(df)

print(df.head(2))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.to_numpy)
print(df.describe())
print(df.dtypes)
print(df.T)
print(df.sort_index(axis=1,ascending=False))
print(df.sort_values(by="B"))
print(df['A'])
print(df[0:3])
print(df["20230101":"20230104"])
print(df.loc[dates[0]])
print(df.loc[:,["A","B"]])
print(df.loc["20230101":"20230104",["A","B"]])


print("\n\nNew\n\n")
print(df.iloc[3])
print(df[df["A"]>0])
df2 = df.copy()
df2["E"] = [ "one","one","two","three","four", "three" ]
print(df2)

