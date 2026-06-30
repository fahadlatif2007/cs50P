def main():
    input_time = input("What time is it? ")
    converted_time = convert(input_time)
    if converted_time >= 7.0 and converted_time <= 8.0:
        print('breakfast time')

def convert(time):
    hours, minutes = time.split(":")
    return(int(hours) + int(minutes) / 60)

    
if __name__ == "__main__":
    main()

