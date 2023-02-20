# ________________________Функции, создания функции, аргументы.______________________

        #****** СЕТ (УДАЛЯЕТ ПОХОЖИЕ ЭЛЕМЕНТЫ И СОЗДАЕТСЯ В ФИГУРНОЙ СКОПКЕ)******

# # users = {"Tom", "Bob",'Alice',"Tom"}
# # print(users)

#    *******ПРЕОБРАЗОВАНИЯ СПИСОК В СЕТ*******

# people = ["Mike", "Bill", "Ted","Bill"]
# people = set(people)
# # people = len(people)
# print(people)

    # ******ФУНКЦИЯ ******

# def say_hello():
#     print("hello")
# say_hello()    
# say_hello()
# say_hello()

# def aiba():
#     print('baicfngndfnfnfmngfmnfm', "gfhgrhsrh","hihshg", "1212")
#     print("huhihi")
# aiba() 

# def say_goodbye():
#     print("say_goodbye")

# say_hello()  
# say_goodbye()


# relate = "s"
# def db_connnect():
#     print("loading")
#     print("connecting")
#     if relate == "s":
#         print("success")
#     else:
#         print("not successful")

# db_connnect()            

    #   ****** АРГУМЕНТЫ*****
#   ******ПОЗИЦИОННЫЕ ОРГУМЕНТЫ******

# def say_hello(name):
#     print(f"hello, {name}")

# say_hello("erjan")

# ******можно добавлять пару аргументов*****

# def say_hello(name,age):
#     print(f"hello, {name}, you are {age}")

# say_hello("erjan",16)
# say_hello("askat",65)s
# say_hello("alice", 45)


# ******Return-возврашает результат****** 

# def sum(a=1,b=1):
#     return a + b 

# res = sum(2,5)
# print(res)
# print(sum(45,778))

# ******вызов аргументов по именам******

# from unicodedata import name


# def say_hello(name,age):
#     print(f"hello, {name}, you are {age}")

# # say_hello(age=22, name="rubik") 
# say_hello("name")
# ******args*****

# def sum( name, age,*args):
#     print(name)
#     print(age)
#     print(args)

# sum(545645,545645,54564,5156,41515,45)

# def sum(*args):
#     print(args)

# sam(45,2,3,89,4,5,56)

# a = 179
# b = 197
# c = (a**2 + b**2) **0.5
# print(c)

# *********

users = {"tom", "bob", "ted", "tom"}
print(users)

people = ["mike", "bill", "tet", "bill"]
people = set(people)
users = str(users)
print(users)