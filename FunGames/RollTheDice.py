import random

def play():
    print("Welcome to Roll The Dice Game!!\n")
    print("You are to roll a dice, the number you roll gets added to your score.")
    print("But if you roll the specific number decided by the system, you lose your score.")
    print("You can always end the game with your current score")

    specific_number=random.randint(1,6)
    print("The specific number is: ", specific_number)
    score=0
    high_score=0

    while True:
        print("Your current score is: ", score)
        choice=int(input("Would you like to roll the dice? (1: Yes, 2: No): "))
        
        if choice>2 or choice<1:
            print("Invalid choice, try again")
        elif choice==1:
            roll=random.randint(1,6)
            print("You rolled the number: ", roll)
            if roll==specific_number:
                print("You lose, your score is reset to 0.\n")
                score=0
            else:
                print("You didnt lose\n")
                score+=roll
        elif choice==2:
            print("You chose to keep your score\n")
            break
        high_score=max(high_score, score)

    print("Your final score is: ", score)
    print("The highest you scored is: ", high_score)
