
list=[10,20,3,4,32,45]
keyword=int(input("Enter the element which is to be searched:"))
for i in range(len(list)):
    if list[i] == keyword:
         print("keyword is matched")
         print("index:",i)
         break
else:
   print("Element is not matched")
   
        
