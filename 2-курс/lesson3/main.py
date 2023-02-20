class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self, year):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print("я еду!")

    def info(self):
        print(f"model:{self.model} year:{self.year}")

    def __str__(self):  # магический метод __str__ - это отображения информации об объекте класса в режиме отладки (для разработчиков)
        return f"model: {self.model} year: {self.year}" 

class ElecticCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(model, year)
        self.__battery = battery

    @property
    def battery(self, battery):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__batetey = value    

    def drive(self):
        print(f"{self.model} я еду используя электричество!") 

    def __str__(self):
        return super().__str__() + f"battery: {self.battery}"

class FuelCar(Car):
    def __init__(self, model, year, fuel_bank):
        Car.__init__(model, year)              
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bank(self, fuel_bank):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank =  value

    def drive(self):
        print(f"{self.model} едет используя топливо!")  

    def __str__(self):
        return super().__str__() + f"fuel_bank:{self.fuel_bank}"

class HybridCar(ElecticCar,FuelCar): # множественное и ромбовидное наследнование
    def __init__(self, model, year, battery, fuel_bank):       
        ElecticCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_bank)

    def drive(self):
        print(f"{self.model} едет используя топливо и электричество!")

tesla = ElecticCar("Tesla model x", 2022, 80000)
bmv = FuelCar("bmv x5", 2020, 60)
lexus = HybridCar("lexus lx-600", 2021, 50000, 40)

tesla.drive()
bmv.drive()
lexus.drive()

print(tesla)
print(bmv)
print(lexus)

print(HybridCar.__mro__)
print(HybridCar.mro())    # __mro__ - это послеедовательность и приаритетность класса