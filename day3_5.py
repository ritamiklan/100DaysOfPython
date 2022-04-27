# Choose your own adventure game *Treasure Island*

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "You came to a crossroad. Do you want to go left or right? Type 'left' or 'right' to start ")

choice1 = choice1.lower()

if choice1 == "right":
    print("You fell into a ditch and died. Game over")
elif choice1 == "left":
    choice2 = input(
        "You arrived to a river. Do you want to swim or wait for a boat? ")
    choice2 = choice2.lower()
    if choice2 == "swim":
        print("You were attacked by crocodiles. Game over")
    else:
        choice3 = input(
            "You arrived on the other shore and you see three doors. Do you want to go in the red, blue, or yellow door? ")
        choice3 = choice3.lower()
        if choice3 == "yellow":
            print("Congrats, you found the treasure!")
        elif choice3 == "blue":
            print("You found an angry wizard who used ice magic on you. Game over.")
        else:
            print("You found an angry dragon who bit your head off. Game over.")
else:
    print("Game over")
