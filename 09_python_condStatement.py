number=int(input("Enter the value: "))
if(number>0):
    print("The number is greater than 0")
elif(number<0):
    print("The number is less than 0 ")
else:
    print("The number is equal to zero")


number1=int(input("Enter the first number: "))
print(number1)
number2=int(input("Enter the second number: "))
print(number2)
number3=int(input("Enter the third number: "))
print(number3)
number4=int(input("Enter the fourth number: "))
print(number4)
if(number1<number2):
    number1=number2
if(number3<number4):
    number3=number4
if(number1<number3):
    number1=number3
print("The largest number among four is : ", number1)


p1="subscribe"
p2="buy now"
p3="donation"
p4="need money"
message=input("Enter the comment: ")
if((p1 in message)or (p2 in message)or (p3 in message)or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment isn't spam")
          

username=input("Enter the username: ")
length=len(username)
if(length<10):
    print("The username has less than 10 characters ")
else:
    print("The username has valid characters")


list=["gajendra",'samyoul','dipak']
name=input("Enter the name you want to search: ")
if(name in list):
    print(f"{name} is present in the list")
else:
    print("invalid")


post=input("Enter the post: ")
if("gajendra" in post.lower()):
    print("Taking about gajendra")
else:
    print("not about gajendra")