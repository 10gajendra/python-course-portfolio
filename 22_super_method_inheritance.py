class Car:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("The car has started...")
    def stop(self):
        print("The cas has stopped...")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().start()
        super().__init__(type)
obj=ToyotaCar("pirus","disel")
print(obj.type)