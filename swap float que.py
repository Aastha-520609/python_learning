# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:19:53 2020

@author: Nageshwor
"""

n=float(input())
temp=1
while(True):
    if(n//temp==0):
        break
    else:
        temp=temp*10

new_num=int(n)/temp
temp=10

while(True):
    if((n*temp)%1==0):
        break
    else:
        temp=temp*10

n=n-int(n)
new_num=new_num+temp*n
print(new_num)
