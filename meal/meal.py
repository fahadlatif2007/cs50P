def main():
    input_time = input("What time is it? ")
    converted_time = convert(input_time)

def convert(time):
    hours, minutes = time.split(":")
    int(hours) + int(minutes/60)
    return

if converted_time >= 7.0 and <= 8.0:
    print('breakfast time')

if __name__ == "__main__":
    main()

