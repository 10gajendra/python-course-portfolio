class A:
    VarA=("Welcome to class A")
class B:
    VarB="welcome to class B"
class C (A,B):
    VarC=("Welcome to class C")
obj=C()
print(obj.VarC)
print(obj.VarB)
print(obj.VarA)
