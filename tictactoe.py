player1_turn = True
player2_turn = False

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]



while True:
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

    #Player Turn Logic
    if player1_turn == True:
        val = int(input('Enter [0 to 8] where you want to insert X: '))
        board[val] = 'x'
        player1_turn = False

    elif player1_turn == False:
        val1 = int(input('Enter [0 to 8] where you want to insert 0: '))
        if board[val1] == 'x':
            print('Please enter a place where x is not entered by player 1')
        else:
            board[val1] = '0'
            player1_turn = True

    #Player Winning Logic
    #Horizontal Win
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x':
        print('Player 1 Wins')
        break

    if board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        print('Player 1 Wins')
        break

    if board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
        print('Player 1 Wins')
        break

    if board[0] == '0' and board[1] == '0' and board[2] == '0':
        print('Player 2 Wins')
        break

    if board[3] == '0' and board[4] == '0' and board[5] == '0':
        print('Player 2 Wins')
        break

    if board[6] == '0' and board[7] == '0' and board[8] == '0':
        print('Player 2 Wins')
        break

    #Vertical Win
    if board[0] == 'x' and board[3] == 'x' and board[6] == 'x':
        print('Player 1 Wins')
        break

    if board[1] == 'x' and board[1] == 'x' and board[7] == 'x':
        print('Player 1 Wins')
        break

    if board[2] == 'x' and board[5] == 'x' and board[8] == 'x':
        print('Player 1 Wins')
        break

    if board[0] == '0' and board[3] == '0' and board[6] == '0':
        print('Player 2 Wins')
        break

    if board[1] == '0' and board[1] == '0' and board[7] == '0':
        print('Player 2 Wins')
        break

    if board[2] == '0' and board[5] == '0' and board[8] == '0':
        print('Player 2 Wins')
        break

    #Digonal Win
    if board[0] == 'x' and board[4] == 'x' and board[8] == 'x':
        print('Player 1 Wins')
        break

    if board[2] == 'x' and board[4] == 'x' and board[6] == 'x':
        print('Player 1 Wins')
        break

    if board[0] == '0' and board[4] == '0' and board[8] == '0':
        print('Player 2 Wins')
        break

    if board[2] == '0' and board[4] == '0' and board[6] == '0':
        print('Player 2 Wins')
        break

    