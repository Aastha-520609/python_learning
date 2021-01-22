
"""R=int(input("Enter no of rows:"))
C=int(input("Enter no of coloumn:"))
matrix1=[]
for i in range(R):
    a=[]
    for j in range(C):
        num=int(input())
        a.append(num)
    matrix1.append(a)
for i in range(R):
    for j in range(C):
         print(matrix1[i][j],end=" ")
    print()"""
    
     
     
                 
R=int(input("Enter no of rows:"))
C=int(input("Enter no of coloumn:"))
print("matrix1")  
matrix1=[]
for i in range(R):
    a=[]
    for j in range(C):
        num=int(input())
        a.append(num)
    matrix1.append(a)
for i in range(R):
    for j in range(C):
         print(matrix1[i][j],end=" ")
    print()
    
print("matrix2")    
matrix2=[]
for i in range(R):
    a=[]
    for j in range(C):
        num=int(input())
        a.append(num)
    matrix2.append(a)
for i in range(R):
    for j in range(C):
         print(matrix2[i][j],end=" ")
    print()
    
print("matrix3")  
matrix3=[[0,0],
         [0,0]]
      

for i in range(R):
    for j in range(C):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
        
for i in range(R):
    for j in range(C):
        print(matrix3[i][j],end=" ")
    print()
    
        
        
        
    