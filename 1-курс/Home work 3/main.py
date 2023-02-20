
namber = [1,2,3,4,5,6,7,8,9,0]
count = 0
for n in namber:
        print(f'{n}-{count}')
        count = count + 1
print(namber)





a = int(input("Введите число а - "))
b = int(input("Введите число b - "))
c = int(input("Введите число c - "))
d = int(input("Введите число d - "))
e = int(input("Введите число e - "))
summa = 0
sub = 0
if a > 0:
    summa = summa + 1
else:
    sub = sub +1
if b > 0:
    summa = summa + 1
else:
    sub = sub +1 
if c > 0:
    summa = summa + 1
else:
    sub = sub +1 
if d > 0:
    summa = summa + 1
else:
    sub = sub +1
if e > 0:
    summa = summa + 1
else:
    sub = sub +1  

print("Количество положительных чисел: ",  summa, "\nКоличество отрицательных чисеел", sub)
        


