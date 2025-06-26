import pandas as pd
data={"id":[1,2,3,4,5,6],"sub":["toc","dccn","mpi","dms","dbms","mefa"],"mid-1":[29,27,19,25,14,27]}
df1=pd.DataFrame(data)
data={"id":[1,2,3,4,5,6],"sub":["toc","dccn","mpi","dms1","dbms1","mefa1"],"mid-1":[27,29,21,27,22,25]}
df2=pd.DataFrame(data)
print(df1.merge(df2,on="id",how="inner"))
print(df1.merge(df2,on="id",how="left"))
print(df1.merge(df2,on=["id","sub"],how="left"))
#print(df1.merge(df2,on="id",how="right"))
print(df1.merge(df2,on=["id","sub"],how="right"))




