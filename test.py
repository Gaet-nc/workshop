import pandas as pd
path_csv = "/Users/gaetan/workshop/data/"
df_trees = pd.read_csv(path_csv+'BD_especes.csv')
print(df_trees.head())
