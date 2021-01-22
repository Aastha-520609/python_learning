#Basic operations in dictionaries
my_dict={1:'apple',2:'ball',3:'cat'}
print(my_dict)
numbers=dict(my_dict)#copying to another dictionary
print(numbers)
print(len(numbers))#printing length of dict
del numbers[2]#deleting the dictionary element
print(numbers)
print(my_dict.keys())
print(my_dict.values())
print(my_dict[3])#in dictionary we can excess key using value but we cannot
                 #excess values value using key.so for this we can do it with
                 #get function
print(my_dict.get(1))
#insert new value to dictionary
my_dict[4]="dog"
print(my_dict)
#updating the actual value
my_dict[2]='parrot'
print(my_dict)
# concatination in dict
dict={5:'orange',6:'pine'}
my_dict.update(dict)
print(my_dict)


      



