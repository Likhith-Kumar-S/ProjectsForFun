import random
from RollTheDiceAuto import autoroll 

def play():
    def update(input_number, number, score, disp=True):
        if disp:
            print("You rolled the number: ", input_number)
        if input_number == number:
            if disp:
                print("You lose, your score is reset to 0.")
            score=0
        else:
            score+=input_number
        if disp:
            print("Your current score is: ", score)
            print()
        return score

    print("Welcome to Roll The Dice Game!!\n")
    print("You are to roll a dice, the number you roll gets added to your score.")
    print("But if you roll the specific number decided by the system, you lose your score.")
    print("You can always end the game with your current score")

    specific_number=random.randint(1,6)
    print("The specific number is: ", specific_number)
    score=0
    high_score=0

    while True:
        choice=int(input("Would you like to roll the dice? (1: Yes, 2: Auto Roll, 3: No): "))

        if choice>3 or choice<1:
            print("Invalid choice, try again")
        elif choice==1:
            roll=random.randint(1,6)
            score=update(roll, specific_number, score)
        elif choice==3:
            print("You chose to keep your score\n")
            break
        elif choice==2:
            l=autoroll()
            for i in l:
                score=update(i, specific_number, score, disp=False)
                high_score=max(high_score, score)
            print("Your current score is: ", score)

        high_score=max(high_score, score)

    print("Your final score is: ", score)
    print("The highest you scored is: ", high_score)
