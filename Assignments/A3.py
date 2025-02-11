import pandas as pd

dataset={'Employee_ID':[101,102,103,104,105],'Name':['A','B','C','D','E'],'Dep':['HR','IT','IT','Marketing','Sales'],'Salary':[50000,70000,65000,55000,60000],'Experience':[2,3,2,2,4],'Joining_Date':['01-01-2018','01-01-2017','01-01-2018','01-01-2018','01-01-2016'],'Gender':['M','F','M','F','M'],'Bonus':[5000,7000,6500,5500,6000],'Rating':[3,4,3,3,5]}

df=pd.DataFrame(dataset)

print(df.dtypes)
print(df.count())