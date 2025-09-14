class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNum(self):
        print(self.real," i + ",self.img," j")
    def __add__(self,num2):
        realNum=self.real + num2.real
        imgNum=self.img + num2.img
        return Complex(realNum , imgNum)
s1=Complex(2,3)
s1.showNum()

s2=Complex(3,4)
s2.showNum()

# s3=s1.add(s2)
# s3.showNum()

s3=s1+s2 #using dunder function
s3.showNum()