import random

count = 0
rolled = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
printedRolls = [' ', ' ', ' ']


rollDice = input("Would you like to roll the dice? (Y or N) ")
if str(rollDice) == 'Y' or 'y':
    while count < 20:
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

sortedRolls = sorted([num1, num2, num3, num4, num5, num6], reverse=True)

if sortedRolls[0] == num1:
    print("The number 1 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num1"
elif sortedRolls[0] == num2:
    print("The number 2 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num2"
elif sortedRolls[0] == num3:
    print("The number 3 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num3"
elif sortedRolls[0] == num4:
    print("The number 4 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num4"
elif sortedRolls[0] == num5:
    print("The number 5 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num5"
else:
    print("The number 6 was rolled ", sortedRolls[0], "times.")
    printedRolls[0] = "num6"

if  sortedRolls[1] == num1 && "num1" not in printedRolls:
    print("The number 1 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num1"
elif sortedRolls[1] == num2 && "num2" not in printedRolls:
    print("The number 2 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num2"
elif sortedRolls[1] == num3 && "num3" not in printedRolls:
    print("The number 3 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num3"
elif sortedRolls[1] == num4 && "num4" not in printedRolls:
    print("The number 4 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num4"
elif sortedRolls[1] == num5 && "num5" not in printedRolls:
    print("The number 5 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num5"
else:
    print("The number 6 was rolled ", sortedRolls[1], "times.")
    printedRolls[1] = "num6"

if sortedRolls[2] == num1 && "num1" not in printedRolls:
    print("The number 1 was rolled ", sortedRolls[2], "times.")
elif sortedRolls[2] == num2 && "num2" not in printedRolls:
    print("The number 2 was rolled ", sortedRolls[2], "times.")
elif sortedRolls[2] == num3 && "num3" not in printedRolls:
    print("The number 3 was rolled ", sortedRolls[2], "times.")
elif sortedRolls[2] == num4 && "num4" not in printedRolls:
    print("The number 4 was rolled ", sortedRolls[2], "times.")
elif sortedRolls[2] == num5 && "num5" not in printedRolls:
    print("The number 5 was rolled ", sortedRolls[2], "times.")
else:
    print("The number 6 was rolled ", sortedRolls[2], "times.")



