import math
s = int(input("Введіть кількість слів "))
l=[]
k = 0
for i in range(s):
    a = input("Введіть слово ")
    l.append(a[0])
for b in l:
    l.remove(b)
    if b in l:
        k+=1
print(k+1)