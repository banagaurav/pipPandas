# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science.


# Series
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# DataFrame 
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd
# This is how we read/load csv(Comma Seperated File)
# r makes it read the path as the values in strings
df = pd.read_csv(r"D:\Code\PipPandas\world_population.csv")
# Too read file in other formats :
# read_json for json files 
# read_excel for excel @ easy right !
# read_table can be used for text files 
# to read txt files in read_csv we need to use ,sep=`operator`
# eg : df = pd.read_csv(r"D:\Code\PipPandas\world_population.csv", sep='\t')


# print(df)

exDf = pd.read_excel(r"D:\Code\PipPandas\world_population_excel_workbook.xlsx")
print(exDf)