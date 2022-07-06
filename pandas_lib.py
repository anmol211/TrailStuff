import pandas as pd

data = pd.DataFrame({"abc": [1, 2, 3],
                     "efg": [2, 3, 4]}, index=["first", "second", "third"])

print(data)
print(data.at["second", "abc"])
print(data.iat[1, 1])
print(data.loc[:, 'abc'])
print(data.iloc[2, 1])
print(data.axes)
print(data.shape)
print(data.size)
print(list(data))


for i, j in data.iterrows():
    print(j)
