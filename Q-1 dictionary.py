# dictionary
dict={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(dict)
dict[6]='f'                                # add the item
print(dict)
print(dict[3])                              # display item with the help of key value
#nested dictionary
dict1={1:'a',2:'b',3:'c',4:'d',5:'e',6:{'a':"first",'b':"second",'c':"third"}} #  neted dictionary
print(dict1)
del[dict[2]]
print(dict)                               # deletion an item with help of key
dict.clear()                               # delete all dict items
print(dict)
dict=dict1.copy()                          #copy dict from existed dict 
print(dict)
print(dict.items())                       #Returns a list containing a tuple for each key value pair
print(dict.keys())                          #Returns a list containing dictionary’s keys
dict={1:"one",2:"two",3:"three",4:"four"}
dict1.update(dict)
print(dict1)                                 #Updatesdictionary with specified key-value pairs
print(dict1.values())                        #Returns a list of all the values of dictionary
dict1.pop(5)
print(dict1)                                   #Remove the element with specified key


