import math
def mod(x, y):
    x0 = 3.0
    y0 = -3.0
    x = x0 - x
    y = y0 - y
    module = math.sqrt(x**2+y**2)
    return module
x1 = float(input("Введіть х точки A: "))
y1 = float(input("Введіть y точки A: "))
x2 = float(input("Введіть х точки B: "))
y2 = float(input("Введіть y точки B: "))
x3 = float(input("Введіть х точки C: "))
y3 = float(input("Введіть y точки C: "))
mod_max = mod(x1, y1)
xe = x1
ye = y1
if mod(x2, y2)>mod_max:
    mod_max=mod(x2, y2)
    xe = x2
    ye = y2
if mod(x3, y3)>mod_max:
    mod_max=mod(x3, y3)
    xe = x3
    ye = y3
print("Найбільша відстань до точки М від точки з координатами:", xe, " ", ye)