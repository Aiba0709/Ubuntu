# КОРТЕЖИ (tupl) - Это те же списки но за одним сключением. Кортежи неизменяемые. 
# Так же как списки они могут состоять из элементов разных типах, перечисленных через запятую. 
# Кортежи заключаются в круглые , а не квадратные скобки. 
# 

# l1 = ("tom","bob","rob","tom","bob","rob")
# print(l1[::-3])
#             # Кортеж и цикл
# l1 = ("tom","bob","rob","tom","bob","rob")
# for item in l1:   
#     print(item)


# СЛОВАРИ (dict) - Это неупорядоченые коллекции произвольных обьектах с доступом по ключу. 

# from collections import UserString


# dict = {
#     "Tom": "Tom@mail.com",
#     "Bob": "Bob@mail.com",
# }
# print(dict[Tom])

# users_list = [
#     [1,"Tom"],
#     [2,"Bob"],
#     [3,"Alice"],
# ]
# # print(users_list[0][1])
# users_dict = dict(users_list)
# print(users_list)
# print(users_dict)

# users = {
#     "+111": "Ulan",
#     "+222": "Tima",
#     "+333": "Uuljan",
# }
# # print(users["+222"])
# users["+444"] = "Askat"
# users2 = users.get("+444")
# del users["+222"]
# users2 = users.copy()
# users2["+666"] = "aiba"
# print(users)
# print(users2)

    #  Словарь и цикл

# from mmap import PROT_READ


# users = {
#     "+111": "Ulan",
#     "+222": "Tima",
#     "+333": "Uuljan",
# }

# for key in users:
#     print(f"{key} - {users[key]}")
    
    

        #   Перебор словаря   

# for i, df in users.items():
#     print(f"{i}-{df}")  

# dict.keys()
# dict.values()

# print(users.keys())   
# print(users.values()) 

    #    комплексный словарь(словарь в словаре)

# users = {
#     "+111": {
#         "name": "Ulan",
#         "phone": "+996709260292",
#         "email": "baimuratovaibek01@mail.com"
#     },
#     "+222": {
#         "name": "tima",
#         "phon": "546435434",
#         "email": "cfhfhjgjg"
#     },
#     "+333": {
#         "name": "aiba",
#         "phon": "48454684",
#         "email":"hffhjvj"
#     },
# }
# print(users)
# print(users["+111"]["name"])







  



