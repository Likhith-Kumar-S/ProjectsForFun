def play():

    def exit():
        return True
        

    def place(player, matrix, symbol):
        while True:
            print(player, "'s turn")
            print("Where do you want to place? ")
            row=int(input("Enter the row number: "))
            col=int(input("Enter the column number: "))
            if (row<1 or row>3 or col<1 or col>3):
                print("Invalid Position! Exiting the Game.")
                exit()
            elif matrix[row-1][col-1] == '-':
                matrix[row-1][col-1] = symbol
                break
            else:
                print("You can't place there. Try again.")

    def win(matrix):
        for i in matrix:
            if i[0]==i[1]==i[2] and i[0]!='-':
                return True
        for j in range(3):
            if matrix[0][j]==matrix[1][j]==matrix[2][j] and matrix[0][j]!='-':
                return True
        if matrix[0][0]==matrix[1][1]==matrix[2][2] and matrix[0][0]!='-':
            return True
        if matrix[0][2]==matrix[1][1]==matrix[2][0] and matrix[0][2]!='-':
            return True
        return False
    
    def printmatrix(matrix):
         for i in matrix:
            for j in i:
                print(j, end=' ')
            print()

    def tie(matrix):
        for i in matrix:
            for j in i:
                if j=='-':
                    return False
        return True

    print("Welcome to Tic Tac Toe Game!\n")
    print("Player 1 is 'X' and Player 2 is 'O'\n")
    print("(To exit the game, enter an invalid position)\n")
    matrix=[['-','-','-'],['-','-','-'],['-','-','-']]
    printmatrix(matrix)


    while True and exit()==True:
        place("Player 1", matrix, 'X')
        printmatrix(matrix)
        print()
        if win(matrix):
            print("Player 1 Wins!")
            break

        if tie(matrix):
            print("It's a Tie!")
            break
        
        place("Player 2", matrix, 'O')
        printmatrix(matrix)
        print()
        if win(matrix):
            print("Player 2 Wins!")
            break

        if tie(matrix):
            print("It's a Tie!")
            break
