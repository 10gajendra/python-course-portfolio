input1=int(input("Enter the number: "))
input2=int(input("Enter the number: "))
input3=int(input("Enter the number: "))
def average(input1,input2,input3):
    avg=(input1 + input2 + input3)/3
    print(f"The average of {input1}, {input2} and {input3} is {avg}")
average(input1,input2,input3)

# Return 
input1=int(input("Enter the number: "))
input2=int(input("Enter the number: "))
input3=int(input("Enter the number: "))
def average(input1,input2,input3):
    avg=(input1 + input2 + input3)/3
    return avg
value=average(input1,input2,input3)
print(f"The average of {input1}, {input2} and {input3} is {value}")


# Default argument
input1=int(input("Enter the number: "))
input2=int(input("Enter the number: "))
def average(input1,input2,input3=6):
    avg=(input1 + input2 + input3)/3
    print(f"The average of {input1}, {input2} and {input3} is {avg}")
average(input1,input2)
