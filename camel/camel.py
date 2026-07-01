#camelCase
#ask user for camelCase
x = input('camelCase: ')

def main():

    for i in x:

        if i.isupper():
           i=('_' + i.lower())
           print(i, end='')

        else:
            print(i, end='')

main()
