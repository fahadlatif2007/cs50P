#camelCase
#ask user for camelCase
x = input('camelCase: ')

def main():

    for i in x:
        print(i)

        if i.isupper():
            return x.replace(i, '_' + i.lower())
        else:
            return i
main()
