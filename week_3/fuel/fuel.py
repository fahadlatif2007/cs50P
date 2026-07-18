def main():
    x, y = get_fraction('Fraction: ').strip().split('/')
    x = int(x)
    y = int(y)
    z = (x / y)*100
    if z>= 99:
        print('F')
    if z<= 1:
        print('E')
    print(f'{int(z)}%')

def get_fraction(prompt):
    while True:
        if prompt == 'Fraction: ':
            try:
                x, y = input(prompt).strip().split('/')
                x = int(x)
                y = int(y)
                if y == 0:
                    raise ValueError
                if x > y:
                    raise ZeroDivisionError
                return f'{x}/{y}'
            except (ValueError, ZeroDivisionError):
                pass

main()
