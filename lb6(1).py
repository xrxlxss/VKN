import math
a=float(input("Введіть число a: "))
b=float(input("Введіть число b: "))
h=float(input("Введіть число h: "))
def ff(x):
    z=x/pow(2,x)+pow(math.e,2)
    return(z)
for i in range (100):
    y=ff(a)
    print(i,'   ',a,'   ',y )
    a=a+h
    if a>b:
        break