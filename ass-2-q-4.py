'''

4) Create a billing program using list. Program should have options to
1. Create Bill=1
2. Display Item Price and total bill amount=2
3. Display Total=3
4. Exit=0
'''
print('''
Create Bill=1
new bill=4
Display Item Price and total bill amount=2
Display Total=3
Exit=0
''')
lst=[]
inp=0

price=0
total=0
n=0
while True:
    inp=int(input("enter the input"))
    if inp==1:
        while True:
            price = int(input("enter the item price,for exit press '0' :"))
            if price==0:
                break
            else:
                lst.append(price)
                total+=price

    elif inp == 0:
            break
    elif inp==2:
        print(lst,end=" ")
        print()
        print("your total bill is : ",total)
        
    elif inp==3:
        print("your total bill is : ",total)
    elif inp==4:
        lst=[]
        total=0
    else :
        print("invalid")
        break


