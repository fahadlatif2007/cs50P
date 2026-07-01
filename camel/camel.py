#camelCase
#ask user for camelCase
x = input('camelCase: ')
for i in x:
    print(i)
if i.isupper():
    replace = i.replace(i, ' ' + i)
    i = i.lower()
    print(i)
