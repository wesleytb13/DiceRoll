import random

count = 0
rolled = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

rollDice = input("Would you like to roll the dice? (Y or N) ")
if str(rollDice) == 'Y' or 'y':
    while count < 10:
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

print("The number one was rolled", num1, "times.")
print("The number two was rolled", num2, "times.")
print("The number three was rolled", num3, "times.")
print("The number four was rolled", num4, "times.")
print("The number five was rolled", num5, "times.")
print("The number six was rolled", num6, "times.")





