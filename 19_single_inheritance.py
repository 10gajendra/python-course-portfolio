class Car:
    color="black"
    @staticmethod
    def start():
        print("The car is started..")
    @staticmethod
    def stop():
        print("The car has stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
print(car1.name)
print(car1.start())
print(car1.stop())
print(car1.color)