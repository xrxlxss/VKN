import math
def func1(x1,x2,x3,x4):
    z=math.sqrt((x2)*(math.cos(x3))+math.pow(math.e,x4))+math.log(2**x1+4,7)
    return(z) 
x=float(input("Введіть число x:"))
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
c=float(input("Введіть число c:"))
z=func1(x,a,b,c)
print(z)