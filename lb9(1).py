import random
spisok1=[" Грудень"," Січень"," Лютий"," Березень"," Квітень"," Травень"," Червень"," Липень"," Серпень"," Вересень"," Жовтень"," Листопад"]
spisok2=["2016","2017","2018","2019","2020","2021, 2022"]
T1=tuple(spisok1)
T=tuple(spisok2)
N=int(input("Введіть кількість "))
for i in range(N):
 z=random.choice(T1)
 r=random.choice(T)
 y=' '
 q=str(random.randint(1,31))
 m=q+z+y+r
 print(m)