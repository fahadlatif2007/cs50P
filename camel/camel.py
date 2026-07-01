#camelCase
#ask user for camelCase
x = input('camelCase: ')
for i in x:
    print(i)
if i.isupper():
    i = i.lower()
    print(i)
