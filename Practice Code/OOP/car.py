class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaBrand(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = ToyotaBrand("Fortuner", "Electric")
print(car1.name)
print(car1.type)
car1.start()
car1.stop()