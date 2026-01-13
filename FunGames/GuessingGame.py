import random

def play():
    print("Welcome to the Guessing Game\n")
    print("There is a Secret Number, Can You Guess It??")
    print("The Secret Number is in Between 1-100")
    print("(You Can Give Up by Entering a Number Greater Than 100 or Lesser than 1)\n")
    number=random.randint(1, 100)
    attempt = 0
    while True:
        guess=int(input("Enter Your Guess: "))
        attempt+=1
        if guess>100 or guess<1:
            print("You Fail :(")
            print("The Secret Number was: ", number)
            break
        elif guess>number:
            print("You guessed a higher number, try something lower.\n")
        elif guess<number:
            print("You guessed a lower number, try something higher.\n")
        elif guess==number:
            print("Congratulations!! You Guessed The Secret Number!!")
            print("You Took {} Attempts to Guess The Secret Number!\n".format(attempt))
            break           
            