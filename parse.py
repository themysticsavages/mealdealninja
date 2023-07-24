import pandas as pd

df = pd.read_csv("data/200recipes.csv", index_col="Unnamed: 0")
print(df.columns)

df2 = df.sort_values(by=["rating", "Price"], ascending=[False, True])
print(df2.head())
