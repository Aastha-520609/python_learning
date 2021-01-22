#if no duplicate value is present
"""list=[10,20,3,4,32,45]
keyword=int(input("Enter the element which is to be searched:"))
for i in range(len(list)):
    if list[i] == keyword:
         print("keyword is matched")
         print("index:",i)
         break
else:
   print("Element is not matched")"""
   
        
#if duplicate value is present
list=[10,20,3,4,32,45,3]
list1=[]
flag=False
keyword=int(input("Enter the element which is to be searched:"))
for i in range(len(list)):
    if list[i] == keyword:
           flag=True
           list1.append(i)
if flag==True:
    print("Keywords are present at index:")    
    for i in list1:
      print(i)         
        
else:
   print("Element is not matched")
   