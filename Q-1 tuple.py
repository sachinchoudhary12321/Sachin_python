#Tuple items are ordered, unchangeable, and allow duplicate values
t1=(1,2,3,4)
t2=('a','b','c','d')
print(t1+t2)                              # concatination in tuple
t3=(t1+t2)                                  #nested tuple 
k=("xyz"*3)
print(k)                                  # repetation in tuple
 # slicing of tuple
print(t1[1:])                            # strting from index 1
print(t1[::-1])                           # reverse of tuple
print(t1[1:3:1])                              # starting index:end index: differnce btw the tuple
del t1                                      # deletion of tuple after it we can't access this tuple
#print(t1)                                   error
#                        methods in tuple
t=(10,20,30,40)
print("minimum",min(t))
print("max",max(t))
print("sum",sum(t))
print("count the occurance of 20",t.count(20))
print("index of given item",t.index(10))