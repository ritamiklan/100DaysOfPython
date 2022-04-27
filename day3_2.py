# nested if/else/elif statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Ticket price is $5.")
        bill = 5
    elif age < 18:
        print("Ticket price is $7.")
        bill = 7
    else:
        print("itcket price is $12.")
        bill = 12

    wants_photo = input("Do you want to buy a photo? Y or N ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your bill is {bill} dollars.")

else:
    print("Sorry, you are too short to ride.")
