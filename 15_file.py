# opening file for reading purpose
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()

# opening file for writing purpose
data="my name is gajendra basnet. Iam a good student"
f=open("demo1.txt","w")
f.write(data)
f.close()