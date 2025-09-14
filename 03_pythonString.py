name=input("Enter the name of your own: ")
print("Good Afternoon",name)
print(f"Good Afternoon {name}")

letter='''Dear <|name|>
your are selected
<|date|>'''
print(letter.replace('<|name|>','Gajendra').replace('<|date|>','24 sept,2050'))

double_space="MY name is Gajendra  Basnet"
print(double_space)
print(double_space.replace('  ',' '))