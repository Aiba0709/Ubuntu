        #  Структуры даных: Списки- методы списков, отрезки.

# sp1 = ["яблока","бананы","капуста","картошка","грибы"]
# print(sp1)

# print(sp1[2])

# sp1[3] = "морковь"
# print(sp1)

# sp1.append("сыр")
# print(sp1)

# del sp1[1]
# print(sp1)

# sp2= [21,23,21,23]
# sp3= [545,356,'gfhf','gg']
# sp4= [sp1,sp2,sp3] 
# print(sp4)
# print(sp4[0][0])

# sp5=[1,2,3]
# sp6=[4,5,6]
# sp7=sp5+sp6
# print(sp7)

# sp8=['f,''g']
# sp9=sp8 * 20
# print(sp9)

# print(sp1[1:3])


# nams = [1,2,3,4]
# people = ["Alihan", "Aibek", "Syimyk", "Murad"]
# list_1 = [True, "Rob", 1, 3.14]
# nambers2 =  list("Hello")
# nambers3 = []

# print(nams)
# print(nambers2)
# print(people[0])

# people = ["Alihan", "Aibek", "Syimyk", "Murad"] 
# people[3] = "Zalkar"
# print(people) 

# people = ["Bob","rob","john"]
# bob, rob, john = people
# print(bob)
# print(john)
# print(rob)

# people = ['bob', 'rob', 'john']
# count = 1
# for person in people:
#     print (f"[person]" - [count])
#     caunt = caunt + 1

# p = ["Tom", "Alice"]
# p2 = ["Todd", "Terk"]
# p.append("Bob")
# p.append(1)
# p.insert(3,"Aibek")
# p.extend(p2)
# index_of = p.index("todd")
# # p.pop(index_of)
# zero_elem = p.pop(0)

# if "Alice" in p:
#     print("Alice ")
#     p.remove("Alice")


# print(p)
# print(p[2:1])
# print([2:5])

# from turtle import wind         





# namber = [1,2,3,4,5,6,7,8,9,0]
# count = 0
# for n in namber:
#         print(f'{n}-{count}')
#         count = count + 1
# print(namber)






# n=[1,2,3,0,-1,-2,-3]
# count = 0
# for nam in n:
#         print(nam)

#    ****** ПОВТОР ******.

# import numbers


# nums = [1, 2, 3, 4]
# people = ["Alihan", "Aibek", "Syimyk", "Murad"]
# list = [True, "Rob", 1, 2, 3]
# numbers2 = list("hello")
# print(nums)
# print(numbers2)
# print(people[0])

# people = ["Alihan", "Aibek", "Syimyk", "Murad"]
# people[0] = "Zalkar"
# print(people) 

# from mmap import PROT_READ


# people = ["Bob", "Rob", "John"]
# bob, rob, john = people
# print(bob)
# print(rob)
# print(john)

# from mmap import PROT_READ


# people = ["Bob", "Rob", "John"]
# count = 1
# for person in people:
#         print(f"{person} - {count}")
#         count = count + 1
# print(person)

# from mmap import PROT_READ


# from operator import index


from operator import index


people = ["Tom", "Alice"]
people.append("bob")
people.insert(3,"aiba")
index_of = people.index("Tom")
print(index_of)