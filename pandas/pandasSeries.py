import pandas as pd

a = [1, 2, 3, 4, 5]
myseries = pd.Series(a)
print(myseries)


# labels
print(myseries[0])      # 1
print(myseries[4])      # 5



# create labels
cups = ["cup1", "cup2", "cup3", "cup4", "cup5"]
myseries1 = pd.Series(cups, index=["a", "b", "c", "d", "e"])
print(myseries1)
