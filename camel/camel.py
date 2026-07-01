#camelCase
#ask user for camelCase

def main():
    x = input('camelCase: ')
    for i in x:

        if i.isupper():
            print('snake_case: ' + '_' + i.lower(), end='')

        else:
            print('snake_case: ' + i, end='')

if __name__ == "__main__":
    main()
