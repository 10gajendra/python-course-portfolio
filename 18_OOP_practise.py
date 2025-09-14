class Student:
    def __init__(self, name,mark):
        self.name=name
        self.mark=mark
    def average_mark(self):
        sum=0
        for value in self.mark:
            sum+=value
            avg=sum/3
        print(f"hi! {self.name} , your average marks is {avg}")
s1=Student("Gajendra",[99,98,100])
s1.average_mark()

class Account:
    def __init__(self, blc , acc_no):
        self.balance=blc
        self.acc_no=acc_no
    def debit(self,amount):
        self.balance-=amount
        print(f"The debited amount is {amount}")
        print("The total balance is ", self.get_blc())
    def credit(self,amount):
        self.balance+=amount
        print(f"The credited amount is {amount}")
        print("The total balance is ", self.get_blc())
    def get_blc(self):
        return self.balance
s1=Account(2000, 123)
s1.debit(100)
s1.credit(200)