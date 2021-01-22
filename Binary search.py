
list=[10,20,5,9,43,56,23,45]
list.sort()
keyword=int(input("Enter the keyword which is to be found:"))
first=0
last=len(list)-1
Found=False
while first<=last and not Found:
    middle_value=(first+last)//2    
    if keyword==list[middle_value]:
        Found=True
    elif keyword>list[middle_value]:
        first=middle_value+1 
    else:
         last=middle_value-1
         
if Found==True:
    print("keyword is found")
else:
    print("keyword is not found")
    
            