import math
a=float(input("Введіть число a: "))
b=float(input("Введіть число b: "))
h=float(input("Введіть число h: "))
n=1
def ff(x):
    z=x/pow(2,x)+pow(math.e,2)
    return(z)
while a<b:
    y= ff(a)
    print(n,'   ',a,'   ',y  )
    a=a+h
    n=1+n