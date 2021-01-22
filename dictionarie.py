dict={}#creating a dictionary
dict['apple']= 150#assigning key  to the dict and the value
dict['banana']=60
dict
print(dict)

#another way to create a dictionary
mail_adress={'aastha':'aastha@gmail.com','pasta':'pasta@gmail.com'}
print(mail_adress)
print(mail_adress.keys())#to print keys of dictionary
print(mail_adress.values())#to print values of dictionary


#creating dict with the help of list
a=[1,2,3,4]
b=['cat','dog','mouse','rat']
my_dict={}#empty dict
for i in range(len(a)):#here we can use any ones lenght because length is equal
    my_dict[a[i]]=b[i]
print(my_dict)

    





