# import msg 
# print(msg.hello)

#         # ****** именованный импорт*****
# from msg import hello
# print(hello)

    #  *****еще один способ импорта*****
# from msg import hello, print_msg
# print_msg("tell")

#     #   *****импортировать все*****
# from msg import *
    #   *****импортировать как букву м*****
# import msg as m
# print(m.hello)
# m.print_msg("tell")

# import math as m
# n1 = m.pow(2, 3)
# print(n1)

# n2 = m.sqrt(9)
# print(n2)

# def sum(a, b):
#     return a+b
# print(sum(2,3))

# sum = lambda a, b: a + b
# print(sum(2,3))

        # *********исключение(найти оошибку)******
# import string

# try:
#     string = input("enter number:")
#     num = int(string)
#     print(num)
# except:
#     print("conversion failed")
# print("end of program")        

# try:
#     string1 = input("enter number:")
#     string2 = input("enter number:")
#     num1 = int(string1)
#     num2 = int(string2)
#     print("Res:", num1/num2)
# except ValueError:
#     print("conversion failed")
# except ZeroDivisionError:
#     print("No nol delit nelza")
# except BaseException:
#     print("Chota poshlo ne tak")        
# print("end of program")


# try:
#     string1 = input("enter number:")
#     string2 = input("enter number:")
#     num1 = int(string1)
#     num2 = int(string2)
#     print("Res:", num1/num2)
# except (ValueError, ZeroDivisionError,BaseException):
#     print("error")     