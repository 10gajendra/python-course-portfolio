words={"sayoj":"help",
       "biralo":"cat",
       "gaai":"cow"}
word=input("Enter the word you want to know the meaning\n")
print(words[word])

sets=set()
element1=int(input("Enter the number\n"))
sets.add(element1)
element2=int(input("Enter the number\n"))
sets.add(element2)
element3=int(input("Enter the number\n"))
sets.add(element3)
element4=int(input("Enter the number\n"))
sets.add(element4)
print(sets)

dict={}
name=input("Enter your name\n")
lang=input("Enter the language\n")
dict.update({name:lang})

name=input("Enter your name\n")
lang=input("Enter the language\n")
dict.update({name:lang})

name=input("Enter your name\n")
lang=input("Enter the language\n")
dict.update({name:lang})

name=input("Enter your name\n")
lang=input("Enter the language\n")
dict.update({name:lang})

print(dict)

dict["gajendra"]='react'
print(dict)