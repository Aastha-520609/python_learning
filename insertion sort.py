l=[1,5,32,67,34,58,98]
for i in range(1,len(l)):
    j=i
    while j>=0 and l[j-1]>l[j]:
        temp=l[j-1]
        l[j-1]=l[j]
        l[j]=temp
        j=j-1
print(l)
        