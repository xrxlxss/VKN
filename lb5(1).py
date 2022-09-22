import math
x=int(input("x="))
if x>0.53:
    y1=3-0.127*x+math.log10(abs(x+2))
    print(("f(x)=",y1))
elif -1.2<x<=0.53:
    y2=math.pow(2.35*math.e**4*x-1)+math.cos(x)
    print(("f(x)="),y2)
elif x<=-1.2:
    y3=0,11*math.sqrt(x+0*3*math.cos(x))
    print(("f(x)="),y3)