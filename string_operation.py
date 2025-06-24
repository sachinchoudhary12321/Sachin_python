x="Hello"
y="World"
# concatination
print(x,y,sep="")
print(x+y)
# function
print(x.lower())  # capital->small
print(x.upper())  #small->capital
print(x.center(120))#print the item after some gap
print(x.title())
print(x.swapcase())#capital->small and small->capital
print(x.capitalize())#More specifically, make the first character have upper case and the rest lower case.
print("h",x.casefold)
print(x.count("l"))#count the given letter un string
print(x.endswith("l"))#assure that the string is end with the given letter
print(x.isalnum())#string is alphanumeric or not
print(x.isnumeric())#string is numeric or not
print(x.isdigit())#string is digit or not