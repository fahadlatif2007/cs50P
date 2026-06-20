#converts :) to 🙂 and :( to 🙁
convert(x)
def convert(x):
    return x.replace(':)', '🙂').replace(':(', '🙁`')
x = input()
print(convert(x))
main()
