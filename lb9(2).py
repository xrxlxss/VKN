import random
a=set()
while not len(a)==100:
    q=random.randint(1,500)
    a.add(q)
print(a)
x=(input("Введіть цілі числа через пробіл"))
s=x.split(' ')
b=set()
for n in s:
    b.add(int(n))
print(b)
w1=a&b
print(w1)
w2=a-b
print(w2)
w3=b-a

print(w3)