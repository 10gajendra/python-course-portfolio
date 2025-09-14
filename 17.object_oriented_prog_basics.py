# # Basics of OOP
class Student:
    name="Gajendra"
s1=Student()
print(s1.name)

# Creating constructor
class Office:
    name="Gajendra"
    # default construtor
    def __init__(self):
        print("Gajendra is hero")
s2=Office()
print(s2.name)

# parameterized constructor and method/ function
class College():
    def __init__(self, name , marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome!",self.name)
    def get_mark(self):
        return self.marks
s1=College("Gajendra",99)
s1.welcome()
print(s1.get_mark())

# static method
class room:
    @staticmethod
    def hello():
        print("hello world")
s=room()
s.hello()


# concept of private attributes
class person:
    __name="Gajendra"
    def __hello(self):
        print("hello")
    def welcome(self):
        self.__hello()
s1=person()
s1.welcome()
