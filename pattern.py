'''
a=int(input("enter a number:"))
for i in range(1,a+1):
    for b in range(i):
        print("*",end='')
    print()
    '''
from base64 import a85decode

'''
a=int(input("enter a number:"))
for i in range(a,0,-1):
    for b in range(i):
        print("*",end='')
    print()
'''
a=int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
a=int(input("enter a number:"))
for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print()