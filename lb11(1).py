file=open("D:\\fileslab\\labelv.txt",'r')
rez=file.read()
f=open("D:\\fileslab\\labelv.txt",'w')
vov = 'aioyue'
for letter in rez:
    if letter in vov:
        f.write(letter)
f.close()
