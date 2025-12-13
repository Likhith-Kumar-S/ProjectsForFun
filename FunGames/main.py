from GuessingGame import play as guess_game

def playagain(game):
    while True:
        print("Would You Like To Play Again?")
        ch=int(input("Enter Your Choice [1: Yes, 2: Quit]: "))
        if ch==1:
            game()
        elif ch==2:
            print("Thank You For Playing!\n")
            break
        else:
            print("Invalid Choice, Try Again\n")

playing=True
while playing:
    print()
    print("=================================")
    print("WELCOME TO GAME LAND")
    print("=================================\n")

    print("Choose a Game You Want To Play\n")
    print("1. Guess Numbers")
    print("2. Quit")
    print()
    choice=int(input("Enter your choice: "))
    print("\n")
    playing=True

    if choice==2:
        playing=False
    elif choice==1:
        guess_game()
        playagain(guess_game)
    else:
        print("Invalid Choice, Try Again\n")