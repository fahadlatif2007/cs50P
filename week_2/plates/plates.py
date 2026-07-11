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

    seen_number = False

    for i in s:
        if i.isdigit():
            if not seen_number:
                if i == "0":
                    return False
                seen_number = True
        elif seen_number:
            return False

    return True


main()