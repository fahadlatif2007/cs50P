def main():
    x, y = get_fraction('Fraction: ').strip().split('/')
    x = float(x)
    y = float(y)
    z = (x / y)*100
    print(f'{int(z)}%')
    if z>= 99:
        print('Full')
    if z<= 1:
        print('Empty')

def get_fraction(prompt):
    while True:
        if 
        try:
            return input(prompt)
        except ValueError:
            pass

main()
