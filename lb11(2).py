import json
d = {}
f =  open("D:\\fileslab\\lab.json", 'r')
for line in f:
    key, *value = line.split()
    d[key] = int(value[0])
f.close()
is_count = int(input("Яку кількість країн ви хочете додати? "))
for i in range(is_count):
    island = input("Введіть назву країни ")
    square = input("Введіть назву та площу столиці ")
    d[island]=square
f =  open("D:\\fileslab\\lab.json", 'w')
for i in d:
    strsquare = str(d[i])
    arg = i + " " + strsquare + "\n"
    f.write(arg)
f.close()