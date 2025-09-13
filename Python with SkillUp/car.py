class car:
    def __init__(self, m, mo, y,p):
        self.make = m
        self.model = mo
        self.year = y
        self.price = p


    def displayInfo(self):
        print("Car Make:", self.make)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
        print("Car Price: $", self.price)

    def getSpeed(self):
        if self.model == "Supra":
            print("280 km/h")  
        else:
            print("Why would drive something else?")     

TOYOTA = car("Toyota", "Supra", 2020, 50000) #this is a instance of the car class

BMW = car("BMW", "M3", 2021, 70000)

obj1 = car("Honda", "Civic", 2019, 20000)#this is a object of the car class

TOYOTA.displayInfo()
TOYOTA.getSpeed()

class Tesla(car):
    def batteryType(self):
        print("Electric Battery")

Tesla = Tesla("Tesla", "Model S", 2022, 80000)
Tesla.batteryType()        