import random
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0


def roll_dice():
    count = 0
    global num1
    global num2
    global num3
    global num4
    global num5
    global num6
    while count < 10:
        rolled = 0
        rolled = random.randint(1, 6)
        print(rolled)
        if int(rolled) == 1:
            num1 = num1 + 1
        elif int(rolled) == 2:
            num2 = num2 + 1
        elif int(rolled) == 3:
            num3 = num3 + 1
        elif int(rolled) == 4:
            num4 = num4 + 1
        elif int(rolled) == 5:
            num5 = num5 + 1
        else:
            num6 = num6 + 1
        count = count + 1


def print_rolls():
    print1 = ""
    print2 = ""
    if sortedRolls[0] == num1:
        print("The number 1 was rolled ", sortedRolls[0], "times.")
        print1 = "num1"
    elif sortedRolls[0] == num2:
        print("The number 2 was rolled ", sortedRolls[0], "times.")
        print1 = "num2"
    elif sortedRolls[0] == num3:
        print("The number 3 was rolled ", sortedRolls[0], "times.")
        print1 = "num3"
    elif sortedRolls[0] == num4:
        print("The number 4 was rolled ", sortedRolls[0], "times.")
        print1 = "num4"
    elif sortedRolls[0] == num5:
        print("The number 5 was rolled ", sortedRolls[0], "times.")
        print1 = "num5"
    else:
        print("The number 6 was rolled ", sortedRolls[0], "times.")
        print1 = "num6"
    if sortedRolls[1] == num1 and print1 != "num1":
        print("The number 1 was rolled ", sortedRolls[1], "times.")
        print2 = "num1"
    elif sortedRolls[1] == num2 and print1 != "num2":
        print("The number 2 was rolled ", sortedRolls[1], "times.")
        print2 = "num2"
    elif sortedRolls[1] == num3 and print1 != "num3":
        print("The number 3 was rolled ", sortedRolls[1], "times.")
        print2 = "num3"
    elif sortedRolls[1] == num4 and print1 != "num4":
        print("The number 4 was rolled ", sortedRolls[1], "times.")
        print2 = "num4"
    elif sortedRolls[1] == num5 and print1 != "num5":
        print("The number 5 was rolled ", sortedRolls[1], "times.")
        print2 = "num5"
    else:
        print("The number 6 was rolled ", sortedRolls[1], "times.")
        print2 = "num6"
    if sortedRolls[2] == num1 and (print1 != "num1" and print2 != "num1"):
        print("The number 1 was rolled ", sortedRolls[2], "times.")
    elif sortedRolls[2] == num2 and (print1 != "num2" and print2 != "num2"):
        print("The number 2 was rolled ", sortedRolls[2], "times.")
    elif sortedRolls[2] == num3 and (print1 != "num3" and print2 != "num3"):
        print("The number 3 was rolled ", sortedRolls[2], "times.")
    elif sortedRolls[2] == num4 and (print1 != "num4" and print2 != "num4"):
        print("The number 4 was rolled ", sortedRolls[2], "times.")
    elif sortedRolls[2] == num5 and (print1 != "num5" and print2 != "num5"):
        print("The number 5 was rolled ", sortedRolls[2], "times.")
    else:
        print("The number 6 was rolled ", sortedRolls[2], "times.")

rollDice = input("Would you like to roll the dice? (Y or N) ")
while rollDice.lower() == 'y':
    roll_dice()
    sortedRolls = sorted([num1, num2, num3, num4, num5, num6], reverse=True)
    print_rolls()
    print(" ")
    rollDice = input("Would you like to roll the dice? (Y or N) ")

print(" ")
print("Thank you, goodbye!")
