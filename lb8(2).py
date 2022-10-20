import numpy as np
import random
M=int(input("Введіть M "))
N=int(input("Введіть N "))
s=[]
a=np.zeros((M,N),dtype=int)
for i in range(M): 
    for j in range (N):         
        a[i][j]=random.randint(1,30) 
print(a)
q=0
while  q<M and q<N:
    q=random.randint(1,20)
print(q)
m=0
n=0
e=0
w=0
b=np.zeros((q,q),dtype=np.int)
for e in range(q)  : 
    for w in range (q):
        b[e][w]=a[m][n]
        n=n+1
        if n==N-1:
            m=m+1
            n=0
        if m==M-1 and n==N-1:
            break

print(b)
