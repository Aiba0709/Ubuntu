
import aiba
n = int(input("Введите число - "))
book = 1 
while book <= n:
    if n % book == 0:
        print(book)
    book += 1    


