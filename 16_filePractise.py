f=open("poem.txt","r")
data=f.read()
if("twinkle" in data.lower()):
    print("twinkle is present in the file:")
else:
    print("Twinkle is absent: ")
f.close()