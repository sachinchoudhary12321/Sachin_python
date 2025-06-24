num=int(input("enter the number of subject : "))
lst=[]
tot=0
for x in range(num):
    k=int(input("enter number of tghe subject"))
    tot+=k
a=tot/num
print(f"percentage is : {a}")
if a >= 60 :
     print("A")
elif a >= 50 :
     print("B")
elif a>=40:
     print("C")
elif a>=33:
    print("D")
else :
    print("FAIL")

