import pandas as pd
df1=pd.DataFrame({"name":["a1","a2","a3","a4"],"marks":[3,2,4,5],"sub":['sub1','sub3','sub4','sub5']})
df2=pd.DataFrame({"name":["b1","b2","b3","b4"],"rank":[1,2,4,5],"sub":['sub1','sub3','sub4','sub5']})
df3=pd.DataFrame({"name":["c1","c2","c3","c4"],"rank":[1,9,3,5],"sub":['sub1','sub3','sub4','sub5']})
df4=pd.concat([df1,df2],keys=['a','b'])
print(df4) # vertically arrange
print(df3.merge(df4,how="leftc:\Users\dell\Downloads\orange_cap.csv",on="sub"))

