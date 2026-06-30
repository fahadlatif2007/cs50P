def main():
    input_time = int(input("What time is it? "))
    converted_time = convert(input_time)

def convert(time):
    hours, minutes = time.split(":")
    return hours + (minutes/60)


if __name__ == "__main__":
    main()

