# ********    ООП (ОБЬЕКТНО ОРИЕНТИРОВАННОЕ ПРОГРАМИРОНИЯ)
# clacc- чертеж.
# self- атрибуты, поля, свойство обьекта
# __init__ - кконструуктор
class Car(Transport):
    wheels = 4
    def __init__(self, model, year, color, pinalties=0 ): 
        self.model = model
        self.year = year
        self.color = color
        self.pinalties = pinalties

    def drive(self, city):
        print(f"машина{self.model} едет в {city}... ")

    def change_color(self, new_color):
        self.color = new_color

mers_car = Car("Mersedes-Benz A52", 2020, "Black", 3000)
kia = Car(model="Kia-Rio", year = 2017, color= "white")

print(type(mers_car)) 
print(f"{mers_car.model}. {mers_car.year}. {mers_car.color} {mers_car.pinalties}")
print(f"{kia.model} {kia.color} {kia.year} {kia.pinalties}")

# ****** перезаписать*****

kia.color = "red"
print(f"{kia.model} {kia.color} {kia.year} {kia.pinalties}")    
print(mers_car.wheels)
mers_car.drive("ош")
kia.drive("бишкек")
kia.change_color("green")

class transport:
    def __init__(self, model, year, color ): 
        self.model = model
        self.year = year
        self.color = color
        