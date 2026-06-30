def main():
    input_time = input("What time is it? ")
    converted_time = convert(input_time)

def convert(time):
    hours, minutes = time.split(":")
    minutes == minutes/60



if __name__ == "__main__":
    main()
