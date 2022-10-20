from array import*
import random 
import numpy as np
a=int(input("Введіть межу"))
b=int(input("Введіть межу"))
arr = array('i',[])
for i in range(10):
   arr.append(random.randint(a,b))
s=np.sort(arr)
print(len(arr), arr[:5])