def ss(w):


    d=w.split(".")
    d=d[-1].rstrip("\n")
    return(d)



s=[]
x='D:\\fileslab\\сайт.txt'
f=open(x,"r")
for line in f:
    s.append(ss(line))
print(s)