class Car:
    @staticmethod
    def start():
        print("The car is started..")
    @staticmethod
    def stop():
        print("The car has stopped..")
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
s1=Fortuner("disel")
s1.start()