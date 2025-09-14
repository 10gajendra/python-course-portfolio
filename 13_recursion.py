def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
value=int(input("Enter the value: "))
print(f"The factorial of {value} is {factorial(value)}")