n = int(input(25))
sum = 0
mult = 1
while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10
    print(suma)
    print(mult)
