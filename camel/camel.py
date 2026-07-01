#camelCase
#ask user for camelCase
x = input('camelCase: ')

def main():

    for i in x:

        if i.isupper():
           i=('_' + i.lower())
           print(i, end='')

        else:
            i=(i)
    print('snake_case: ' + i)

main()
