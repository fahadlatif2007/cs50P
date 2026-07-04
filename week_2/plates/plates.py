def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if len(s) > 2 and s[2:].isdigit() and s[2] == '0':
        return False
    return True
    ...


main()
