def displayBoard(status):
    print( status['7'] + '|' + status['8'] + '|' + status['9'] )
    print("------")
    print( status['4'] + '|' + status['5'] + '|' + status['6'] )
    print("------")
    print( status['1'] + '|' + status['2'] + '|' + status['3'] )
    return(status)

theBoard = {'7' : ' ' , '8' : ' ' , '9' : ' ' ,
            '4' : ' ' , '5' : ' ' , '6' : ' ' ,
            '1' : ' ' , '2' : ' ' , '3' : ' ' }

def game(player1, player2):
    turn = 'x'
    count = 0
    player = player1

    for count in range(10):
        displayBoard(theBoard)
        print("\nIt is your turn " + player + " Put your choice..\n")
        move = input("Enter (" + turn + ") at : ")

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count = count + 1
        else:
            print("This place is filled")
            print("Move to which place ?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # for top row
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # for middle row
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # for bottom row
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # for left column
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # for middle column
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # for right column
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # for a diagonal
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # for another diagonal
                displayBoard(theBoard)
                print("\nGame Over\n")
                print("*-*-*-* " + player + " won *-*-*-*")
                break

        if turn == 'x':
            turn = 'o'
        elif turn == 'o':
            turn = 'x'

        if player == player1:
            player = player2
        elif player == player2:
            player = player1

        if count == 9:
            print("\n.....Game Over.....")
            print("It is a tie !!!!\n")
            displayBoard(theBoard)
            break

if __name__ == '__main__':
    print("\n 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 \n")

    a = input("\nEnter name of player 1 = ")
    if a == '':
        a = input("Enter your name\n(Caution :- or if you give a space your name will be just a space) :")

    b = input("\nEnter name of player 2 = ")
    if b == '':
        b = input("Enter your name\n(Caution :- or if you give a space your name will be just a space) :")

    if a == b:
        print("\nBoth the name are same..")
        b = input("\nPlayer B please change your name \n(Caution :- if the name is again same, both the players name will be given as same) : ")
        if b == ' ':
            b = input("Enter your name again :")

    print("\n{0} will put x in the game and {1} will put o in the game.\n".format(a,b))

    game(a, b)

    restart = input("\nWould you like to play the game again? [Y,n] :- ")
    if (restart =='y' or restart == ''):
        print("\n*-*-* Hurrah!! the game starts again!!! *-*-*\n")
        c = input("\nEnter name of player 1 \n(If you enter name as 'same' then ur name will be he same as it was)= ")
        if c == '':
            c = input("\nEnter your name\n(Caution :- or if you give a space your name will be just a space) :")

        d = input("\nEnter name of player 2 \n(If you enter name as 'same' then ur name will be he same as it was)= ")
        if d == '':
            d = input("\nEnter your name\n(Caution :- or if you give a space your name will be just a space) :")

        if c == d:
            print("\nBoth the name are same..")
            d = input("\nPlayer B please change your name \n(Caution :- if the name is again same, both the players name will be given as same) : ")
            if d == ' ':
                d = input("\nEnter your name again :")

        if (c == 'same' or c == 'Same'):
            c == a

        if (d == 'same' or d == 'Same'):
            d == b

        theBoard = {'7' : ' ' , '8' : ' ' , '9' : ' ' ,
            '4' : ' ' , '5' : ' ' , '6' : ' ' ,
            '1' : ' ' , '2' : ' ' , '3' : ' ' }
        game(c, d)

    if restart == 'n':
        print("\nThanks for playing !!!!!! See you both later !!!!!!\n")

    else:
        print("\nThanks for playing !!!!!! See you both later !!!!!!\n")
