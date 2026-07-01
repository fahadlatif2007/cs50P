#camelCase
#ask user for camelCase
x = input('camelCase: ')

def main():

    for i in x:
        print(i, end='')

        if i.isupper():
            print('_' + i.lower(), end='')
        else:
            print(i, end='')

main()
