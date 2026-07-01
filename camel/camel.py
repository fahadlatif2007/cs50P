#camelCase
#ask user for camelCase
x = input('camelCase: ')

def main():

    for i in x:
        print(i, end='')

        if i.isupper():
            i=x.replace(i, '_' + i.lower())
        else:
            print(i)

main()
