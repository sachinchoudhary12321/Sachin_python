def div(a,b):
    if b==0:
        print("input is not valid ")
    else:
        d=a/b
        print(f"division of {a} and {b} is : ",d)
x=int(input("enter the a"))
y=int(input("enter the b"))
div(x,y)