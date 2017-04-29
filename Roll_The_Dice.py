import random

def dice(sides=6):
    roll_dice = random.randint(1,sides)
    return roll_dice

def main():
    sides = 6
    going = True
    while going:
        hey = input("Ready to roll the dice? ENTER=roll. Q=Exit. ")
        if hey.lower() != "q":
            roll_dice = dice(sides)
            print ("You rolled a:", roll_dice)
        else:
            going = False

    print("Thanks for playing")

main()
