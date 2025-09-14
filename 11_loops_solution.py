number=int(input("Enter the number you want to multiply: "))
for i in range(1,11):
    print(f"{number} x", i ,"=",i*number)


list=["Gajendra","Samyoul","Shyam","deepak"]
for item in list:
    if(item.startswith("S")):
        print(f"hello, {item}")


table=int(input("Enter the number which table you want: "))
i=1
while(i<11):
    print(f"{table} x ",i,'=',i*table)
    i+=1


value=int(input("Enter the value: "))
for i in range(2,value):
    if(value % i == 0):
        print("The number is not prime ")
        break
else:
    print("The number is prime ")


digit=int(input("Enter the value: "))
i=0
sum=0
while(i<=digit):
    sum+=i
    i+=1
print(sum)


n=int(input("Enter the value: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"The factorial is {fact} ")


number=int(input("Enter the number you want to multiply: "))
for i in range(10,0,-1):
    print(f"{number} x", i ,"=",i*number)
