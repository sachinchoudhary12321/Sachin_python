#find the smallest number in list
lst=[]
val=0
inp=0
m=0
m2=0
n=0
t=0
n=int(input("enter the lenth of list"))
for x in range(n):
    val=int(input("enter the value"))
    lst.append(val)
    m=lst[0]
    # smallest
for x in lst:
    if m>x:
        m=x
print(m,"is samllest")

#second smallest

for x in lst:
    if x!=m :
        if m2==0:
            m2=x
        elif m2!=0 :
            if m2>x:
                m2=x

print(m2,"second lowest")
#greatest
for x in lst:
    if m<x:
        m=x
print(m,"is greatest")
# second greatest
m2=0
for x in lst:
    if x!=m :
        if m2==0:
            m2=x
        elif m2!=0 :
            if m2<x:
                m2=x
print(m2,"second greatest")