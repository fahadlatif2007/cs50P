#converts :) to 🙂 and :( to 🙁
def main():
    x = input()
    print(convert(x))

def convert(x):
    return x.replace(':)', '🙂').replace(':(', '🙁`')

main()
