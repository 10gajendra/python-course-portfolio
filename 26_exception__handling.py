firstNum=int(input("Enter the first number: "))
secondNum=int(input("Enter the second number: "))
try:
    print(firstNum/secondNum)
except Exception as e:
    print(f"error occured is \"{e}\"")