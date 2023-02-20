    # ************* инкапсуляция ***********
# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
# Инкапсуляция делает некоторые из компонент доступными только внутри класса.
# Инкапсуляция в Python работает лишь на уровне соглашения между программистами о том,
#  какие атрибуты являются общедоступными, а какие — внутренними.

class  Address:
    def __init__(self,city, street, number ):
        self.__city = city
        self.__street = street
        self.__number = number
       
        

class Person:
    def __init__(self,name, age, city, street, number ):
        self.__city = city
        self.__street = street
        self.__number = number

    
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value       

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value    
        
class Animal:
    def __init__(self, name, age, city, street, number):
        self.__name = name      # lдва нижний пробел вскрытие аргументов(МАДИФИТАТОР)
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise AttributeError(  "неверный тип атрибута")
        self.__city = city
        self.__street = street
        self.__number = number
        self.__is_born()        

    def get_name(self):        # геттер — это метод, который возвращает (от слова get) нам значение какого-то поля
        return self.__name

    def set_naame(self, value): #сеттер — это метод, который изменяет (устанавливает; от слова set) значение поля
        self.__name = value
        # ****** ДИКАРАТОР ***********    
    @property                  # второй способ написать гееттер
    def age(self):
        return self.__age        
            
    @age.setter               # второй способ написть сеттер
    def age(self, value):
        if  isinstance(value, int) and value >0:   
            self.age = value
        else:
            raise AttributeError("неверный тип атрибута")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value       

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value    

    def __is_born(self):
        print(f"родилась животное {self.__name}")
    

animal = Animal("Jivotnoe", 3)
# print(animal.get_name())
print(animal.age)
# animal.set_naame("Ak-tosh")
animal.age = 5

# print(animal.get_name())
print(animal.age)
# print(f"{animal.name}, {animal.age}")

# animal.age = -5
# print(f"{animal.name}, {animal.age}")

