def greatest(a,b,c):
    if(a>b and a>c):
        print(f"The greatest number among {a},{b} and {c} is {a}")
    elif(b>a and b>c):
        print(f"The greatest number among {a},{b} and {c} is {b}")
    else:
        print(f"The greatest number among {a},{b} and {c} is {c}")
input1=int(input("Enter the number: "))
input2=int(input("Enter the number: "))
input3=int(input("Enter the number: "))
greatest(input1, input2, input3)
def temp_conversion(celcius):
  f=((celcius/100)*180)+32
  return f
celcius=int(input("Enter the temperature in celcius: ")) 
print(f"The conversion of {celcius} degree celcius into fahrenit is {temp_conversion(celcius)}")


#  sum of n natural number using recursion
number = int(input("Enter the number upto  which you want to add: "))
def natural_number_addtion(n):
    if(n==1):
        return 1
    return  natural_number_addtion(n-1)+n
function_call=natural_number_addtion(number)
print(f"The sum is {function_call}")