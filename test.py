import pandas as pd
# This is how we read/load csv(Comma Seperated File)
df = pd.read_csv(r"D:\Code\PipPandas\world_population.csv")
# Too read file in other formats is easy
# read_json for json files 
# read_excel for excel @ easy right ! 
print(df)