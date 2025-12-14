import random

def play():
    print("Welcome To Rock Paper Scissors\n")
    print("You Win if you have more wins than loses or ties.")
    print("(To exit you can enter a value greater than 3 or lesser than 1)")
    number_of_times=int(input("Enter the number of rounds you want to play: "))

    moves=["Rock", "Paper", "Scissor"]
    tie, win, loss = 0, 0, 0

    for i in range(number_of_times):
        computer_choice=random.randint(1,3)-1
        print("1. Rock\n2. Paper\n3. Scissor")
        user_choice=int(input("Enter your choice: "))

        if user_choice>3 or user_choice<1:
            print("Exiting game\n")
            break
        elif user_choice-1==computer_choice:
            print("It's a tie!")
            tie+=1
        elif user_choice==1 and computer_choice==2:
            print("You win!")
            win+=1
        elif user_choice==2 and computer_choice==0:
            print("You win")
            win+=1
        elif user_choice==3 and computer_choice==1:
            print("You win")
            win+=1
        else:
            print("You lose!")
            loss+=1
        print("The Computer choose: ", moves[computer_choice])
        print()

    print("The scores:")
    print("Wins: ", win, "\nLoss: ", loss, "\nDraws: ", tie)

    l=[win, loss, tie]
    m=l.index(max(l))
    if win!=loss and loss!=tie:
        if m==0:
            print("You Won The Game!!")
        elif m==1:
            print("You Lose The Game :(")
        else:
            print("The Game Was A Draw :(")
    elif win==loss:
        print("The Game Was A Draw :(")
    elif loss==tie:
        print("The Game Was A Draw :(")
    else:
        print("You Won The Game!!")