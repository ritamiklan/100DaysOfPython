# leapyear

year = int(input("Which year to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# leap: evenly divisible by 4: Y
# leap: evenly divisible by 100: N
# leap: evenly divisible bt 400: Y
