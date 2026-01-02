import pandas as pd

df = pd.read_csv(r"D:\Code\PipPandas\world_population.csv")
# print(df)

# syntax goes like 
# df[df[' column Name '] >= condition] 
print("records which have Rank less than equal to 10")
print(df[df['Rank'] <= 10])

# This one is like LIKE in SQL
print('filtering the records of specific countries')
specific_countries = ['Brazil', 'Bangladesh']
print(df[df['Country'].isin(specific_countries)])

# Countries that contains United
print('Countries that contains United using contains()')
print(df[df['Country'].str.contains('United')])
# making another dataFrame df2 from df , setting index 'Country'
df2 = df.set_index('Country')
print(df2)

# using filter function
# syntax : df.filter(items = [ columns Name ])
print(df2.filter(items = ['Continent', 'CCA3']))

# countries that has uninted
print('Countries that contains United using like ')
print(df2.filter(like = 'United' , axis= 0 )) # axis = 0 means search in the index rows  , where as axis  = 1 means search in columns names

# using loc in dataframe will give us info of that record 
# loc['record index can be name such as "USA" ']
print('Using .loc[`''`]')
print(df2.loc['United States'])

# where as iloc[] is integer location returns same kind of output as loc

# ++++ OrderBy ++++
print('using order by')
print(df[df['Rank']< 10].sort_values(by = 'Rank', ascending=True))

# too order by using multiple columns we need to give column name in by as a list 
# such as .sort_values(by = ['column1','column2'])