import csv
address=[['name','address','mobile'],
         ['sachin','jaipur','9087'],
         ['naveen','mumbai','7890'],
         ['ram','delhi','delhi']]
with open('address.csv','w',newline="") as file:
    a=csv.writer(file)
    for x in address:
        a.writerow(x)