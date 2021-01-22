
string=input()
set1=set(string)
set2=set({'A','C','T','G'})
if (len(string)>0 and set1==set2):
    a=string.count('A')
    t=string.count('T')
    g=string.count('G')
    c=string.count('C')
    print("A")
    print(a)
    print("T")
    print(t)
    print("C")
    print(c)
    print("G")
    print(g)
else:
    print("Invalid input")
    
    