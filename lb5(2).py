import math
x=float(input("Введіть координату A x:"))
y=float(input("Введіть значення A y:"))
c=float(input("Введіть значення B x:"))
b=float(input("Введіть значення B y:"))
u=float(input("Введіть значення C x:"))
p=float(input("Введіть значення C y:"))
s1=math.sqrt(math.pow(x,2)+math.pow(y,2))
s2=math.sqrt(math.pow(c,2)+math.pow(b,2))
s3=math.sqrt(math.pow(u,2)+math.pow(p,2))
q=str("Це координата А")
m=str("Це координата B")
o=str("Це координата C")
if(s1>s2)and(s1>s3):
    print(q)
if(s2>s1)and(s2>s3):
    print(m)
if(s3>s1)and(s3>s2):
    print(o)

