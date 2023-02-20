# ДЗ*:
# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись
# арифметические вычисления с атрибутами объекта cpu и memory.
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# 3. Добавить сеттеры и геттеры к существующему атрибуту.
# 4. Добавить в класс Phone метод call с входящим параметром sim_card_number и
# call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от
# переданного номера сим-карты (например: если при вызове метода передать число 1 и
# номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с
# сим-карты-1 - Beeline).
# 5. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 6. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который
# бы распечатывал симуляцию проложения маршрута до локации.
# 7. В каждом классе переопределить магический метод __str__ которые бы возвращали
# полную информацию об объекте.
# 8. Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно
# было сравнивать между собой объекты, по атрибуту memory.
# 9. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 10. Распечатать информацию о созданных объектах
# 11. Опробовать все возможные методы каждого объекта (например: use_gps и тд.)

class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory

    @property

    def cpu(self):
        return self.__cpu


    @cpu.setter
    
    def cpu(self,value):
        self.__cpu = value


    @property

    def memory(self):
        return self.__memory


    @memory.setter
    
    def side_b(self,value):
        self.__memory = value


    def make_computations(self):
        print({self.cpu} - {self.memory})


    def __str__(self):
        return super().__str__() + f'{self.cpu} - {self.memory}'



    def __add__(self, other):
        return self.__memory + other.__memory

    def __sub__(self, other):
        return self.__memory - other.__memory

    def __mul__(self, other):
        return self.__memory * other.__memory

    def __floordiv__(self, other):
        return self.__memory // other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def info (self):
        return f'{self.cpu} - {self.memory}'





class Phone:
    def __init__(self,sim_card_list, sim_card_number, call_number):
        self.__sim_card_list = sim_card_list
        self.sim_card_number = sim_card_number
        self.call_number = call_number


    @property

    def sim_card_list(self):
        return self.__sim_card_list


    @sim_card_list.setter
    
    def sim_card_list(self,value):
        self.__sim_card_list = value



    def call (self):
        print(f'идет звонок на номер{self.sim_card_number}, с симкарты{self.call_number} ')



    def __str__(self):
        return super().__str__() + f'идет звонок на номер{self.sim_card_number}, с симкарты{self.call_number} '

    def info (self):
        return {self.sim_card_number}, {self.call_number}




class SmartPhone(Computer,Phone):
    def __init__(self,location):
        self.location = location

    def use_gps (self):
        print(f'построен маршрут этой локации {self.location}')


    def __str__(self):
        return super().__str__() + f"построен маршрут этой локации {self.location} "
         
    def info (self):
        return {self.location}


computer = Computer (cpu= 5, memory=4)

phone = Phone (sim_card_list= 2 , sim_card_number= +996709260292 , call_number= 1)

smartPhone1 = SmartPhone (location= 'A.Baimuranov')    
smartPhone2 = SmartPhone (location= 'Ch.Denizov')    



gadjet = [computer, phone, smartPhone1, smartPhone2]


for p in gadjet:
    
    print(p.info())




        
                                          
                        