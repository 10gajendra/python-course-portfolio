class Person:
    name="Dipak"
    @classmethod
    def namechange(cls,name):
        cls.name=name
obj=Person()
obj.namechange("Gajendra")
print(obj.name)
print(Person.name)