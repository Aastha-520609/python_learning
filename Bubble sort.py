
l=[]
n=int(input("Enter the no of list:"))
num=0
temp=0
for i in range(0,n):
    num=int(input())
    l.append(num)
print("unsorted list",l)
for j in range (len(l)-1):
    for i in range(len(l)-1-j):
          if l[i]>l[i+1]:
           temp=l[i]
           l[i]=l[i+1]
           l[i+1]=temp
           print(l)
          else:
              print(l)
    print() 
print("sorted list",l)
         