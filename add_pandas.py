import pandas as pd

df = pd.read_csv("/mnt/data/foo/numbers.csv")

df["sum"] = df["a"] + df["b"]

print("*************************")
print(df)
print("*************************")

df.to_csv("outputs/sum.csv", index=False)
