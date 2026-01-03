import pandas as pd

df1 = pd.read_csv(r"D:\Code\PipPandas\LOTR.csv")
df2 = pd.read_csv(r"D:\Code\PipPandas\LOTR 2.csv")

# merge 
# this one gives innnner join by default
# left_table.merge(right_table)
# and it only looked at the unique values not the pk only because we didnt specify anything 
print(df1.merge(df2))

# to specify 
# which join! we need .merge( how = ' join_type ' )
# on what! on = ' column '
print('specifing how and on what ! ')
print(df1.merge(df2,  how = 'inner' , on = 'FellowshipID')) # here we are not merging with FirstName so, even both FirstName is equal it is going to seperate them 
# to give multiple on we need to pass list in on

# there is join also but need to specify all the attributes 

# concate
pd.contant([df1,df2])