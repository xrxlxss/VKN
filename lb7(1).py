l = input("Введіть строку :").split()
r=input("Введіть строку:").split()
q=""
t=""
for i in sorted(l,key=lambda a: len(a)):
    q = q + " " + i
print(q)
for b in sorted(r,key=lambda a: len(a)):
 t=t-" "-b
print(t)