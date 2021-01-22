
l=[34,65,3,67,98,32]
print("unsorted list",l)
for i in range(len(l)):
    min_value=min(l[i:])
    min_ind=l.index(min_value)
    temp=l[i]
    l[i]=l[min_ind]
    l[min_ind]=temp
    print(l)
    