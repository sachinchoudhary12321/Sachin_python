#set
# unordered,unchangeable,unindexed,can't allow the duplicate value
s={1,2,3,4,5}
s.add(1)
print(s)
s1={"a","b","c"}
s3=s1.union(s)                                         # union
print(s3)
print(s1.intersection(s3))                             # intersaction
print(s1.difference(s3))                               # difference
s1.clear()
print("set is : ",s1)                                  #all the item in set are remove
