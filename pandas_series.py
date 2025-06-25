# pandas series by the dictionary
import pandas as pd
dic={1:"A",2:"B",3:"C",4:"D"}
myvar=pd.Series(dic)
print(myvar)
#pandas series by the list
l=[1,2,3,4,5]
myvar=pd.Series(l)
print(myvar)
#access the element in pandas
print(myvar[0])                      # for accessing the elemement we have to give the index number

