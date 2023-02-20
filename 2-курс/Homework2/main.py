
# ХОМЕ ВОРК:
# 1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и
# присвоить ему значение cm (сантиметры) или mm (миллиметры)
# 2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть
# атрибутов уровня объекта.
# 3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади
# фигуры)
# 4. Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о
# фигуре)
# 5. Создать класс Circle (круг), наследовать его от класса Figure.
# 6. Добавить в класс Circle атрибут radius (радиус круга), атрибут должен быть приватным.
# 7. В классе Circle переопределить метод calculate_area, который бы считал и возвращал площадь
# круга.
# 8. В классе Circle переопределить метод info, который бы распечатывал всю информацию о круге
# следующим образом: Например - Circle radius: 2cm, area: 12.57cm.
# 9. Создать класс RightTriangle (прямой треугольник - 90 градусов), наследовать его от класса Figure.
# 10. Добавить в класс RightTriangle атрибут side_a (сторона а) и side_b (сторона б), атрибуты должны
# быть приватными.
# 11. В классе RightTriangle переопределить метод calculate_area, который бы считал и возвращал
# площадь треугольника.
# 12. В классе Triangle переопределить метод info, который бы распечатывал всю информацию о
# треугольнике следующим образом: Например - RightTriangle side a: 5cm, side b: 8cm, area: 20cm.
# 13. В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников 14. Затем
# через цикл вызвать у всех объектов списка метод info


from xml.sax.handler import DTDHandler


class Figura:
    unit =("mm")
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figura):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        a = 4.66 * self.__radius
        return a

    @property
    def radius (self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.radius = value

    def info(self):
        print(f"r:{self.__radius}, p:{self.calculate_area()} ")

class RightTriangle(Figura):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a (self, value):
        self.__side_a = value

    
    @property
    def side_b(self):
        return self.__side_b

    @side_a.setter
    def side_b (self, value):
        self.__side_b = value

    def calculate_area(self):
        a = self.__side_a * self.__side_b / 2
        return a

    def info(self):
        print(f"a:{self.__side_a}, b:{self.__side_b}, площадь: {self.calculate_area()}")

krug1 = Circle(radius=2)
krug2 = Circle(radius=10)
tri1 =  RightTriangle(side_a=9, side_b=10)
tri2 =  RightTriangle(side_a=42, side_b=56)
tri3 =  RightTriangle(side_a=100, side_b=200)

pole = [krug1,krug2,tri1,tri2,tri3]

for pole in pole:
    pole.calculate_area()
    pole.info()        
 




                      
