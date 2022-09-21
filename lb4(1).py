import math
x=float(input("введіть x:"))
y=math.pow(3,-x)*(math.fabs(3.19*x))+math.log(math.fabs(x+1),4)/(math.fabs(x+1)+0.7)
print(y)