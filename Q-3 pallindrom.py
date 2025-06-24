x=int(input("enter the number : "))
y=x
n=0
v=0
val=0
while True:
    if x>0:
       
        x//=10
        n+=1

    else:
        break
x=y
while True:
    if n>0:
        v=x%10
        x//=10
        n-=1
        val=v*10**n+val
      
        
    else:
        break
print(val)
if y==val :
    print("pallindrom")
else:
    print("not a pallindrom")