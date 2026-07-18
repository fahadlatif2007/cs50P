def main():
    x, y = get_fraction('Fraction: ')
    x = int(x)
    y = int(y)
    z = (x / y)*100
    z = round(z)
    if z>= 99:
        print('F')
    elif z<= 1:
        print('E')
    else:
        print(f'{z}%')

def get_fraction(prompt):
    while True:
        if prompt == 'Fraction: ':
            try:
                x, y = input(prompt).strip().split('/')
                x = int(x)
                y = int(y)
                if y == 0:
                    raise ZeroDivisionError
                if x > y:
                    raise ValueError
                if x == -
                return (x, y)
            except (ValueError, ZeroDivisionError):
                pass

main()
