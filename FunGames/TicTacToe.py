def play():
    def place(player, matrix, symbol):
        while True:
            print(player, "'s turn")
            print("Where do you want to place? ")
            row=int(input("Enter the row number: "))
            col=int(input("Enter the column number: "))
            if matrix[row-1][col-1] == '-':
                matrix[row-1][col-1] = symbol
                break
            else:
                print("You can't place there. Try again.")

    while True:
        matrix=[['-','-','-'],['-','-','-'],['-','-','-']]
        for i in matrix:
            for j in matrix:
                print(j, end=' ')

        print()
        