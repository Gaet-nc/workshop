import pandas as pd
path_csv = "/Users/gaetan/workshop/data/"
df_trees = pd.read_csv(path_csv+'BD_especes.csv')
tosave = df_trees.head()
tosave.to_csv(path_csv+'results.csv')
