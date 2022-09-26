import random
import math
b=float(input("Введіть верхню межу табулювання: "))
a=float(input("Введіть нижнью межу табулювання:  "))
h=float(input("Введіть крок табулювання: "))
sp=[]
sp1 = []
def f(x):
    z=x/pow(2,x)+pow(math.e,2)
    return(z)
for i in range (100):
    y= f(a)
    a= round(a,2)
    y= round(y,4)
    sp.append(y)
    a=a+h
    if a>b or a == b:
        break
random.shuffle(sp)
print(sp)
sp.sort(reverse= True)
print(sp)