# tip calcualtor
print("Welcome to the tip calculator")
amount = float(input("What was the total bill? $100"))

percentage = input("What percentage tip to give? ")

people = int(input("How many people to split the bill? "))

multiplier = (int(percentage) / 100) + 1

result = round((amount * multiplier / people), 2)

print(f"Each person should pay: ${result}")
