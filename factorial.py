n=int(input("enter an number"))
k=n
p=1
for x in range(n):
    p*=n
    n-=1
print(p,"is the factorial of ",k)