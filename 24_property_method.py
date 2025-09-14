class Percentage:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
    @property
    def percent(self):
        return str((self.phy+self.che+self.math)/3) + "%"
obj=Percentage(95,55,100)
print(obj.percent)
obj.phy=34
print(obj.percent)