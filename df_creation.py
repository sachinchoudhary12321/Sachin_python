# create dataframe by  2D list
import pandas as pd

l=[[1,2,3,],[4,5,6],[7,8,9]]
x=pd.DataFrame(l)
print(x)
# from dict
d={1:[1,2,3,4,5],2:[2,3,4,5,6],3:[3,4,5,6,7],4:[4,5,6,7,8],5:[5,6,7,8,9]}   # all the list have same length
y=pd.DataFrame(d)
print(y)
# list of lists
l=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
q=pd.DataFrame(l)
#list of tuple
print(q)
t=[(1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15)]
q=pd.DataFrame(t)
print(q)
#list of dict
l=[{1:{1,2,3,4,5},2:{11,12,13,14,15},3:{21,22,23,24,25}},{2:{16,17,18,19,20},1:{6,7,8,9,10},3:{}},{3:{11,12,13,14,15}}]
q=pd.DataFrame(l)
print(q)
