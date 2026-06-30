def main():
    input_time = input("What time is it? ")
    converted_time = convert(input_time)

def convert(time):
    hours, minutes = time.split(":")
    return float(hours + (minutes/60))

if converted_time >= 7.0 and <= 8.0
    print('breakfast time')

if __name__ == "__main__":
    main()

