#camelCase
#ask user for camelCase
def main():
    x = input('camelCase: ')
    for i in x:
        print(i)
    if i.isupper():
        return x.replace(i, '_' + i.lower())

main()
