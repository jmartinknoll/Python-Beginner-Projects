''' tic-tac-toe game. Objective: represent the board, change between X and O every move, have user input for 
entering moves, make sure moves go to the correct place on the board, check for wins (8 possible win states), 
check for a tie (full board with no win state), offer the choice to start a new game, debug any code that
has user input. '''



# each key represents a square, location is where the number is located on a number pad on a computer
# each value will be blank to start, later changed to X or O via user input

board_state = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}


# this code will be used later to clear the board should the players choose to play another game
board_keys = []
for key in board_state:
    board_keys.append(key)


def print_board(board):
    
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def play_game():

    turn = 'X'
    count = 0
    win = False
    draw = False

    print('To choose a square, enter a number 1-9. From left to right:')
    print('7-8-9 represents the top row, 4-5-6 the middle row, 1-2-3 the bottom row.')
    print_board(board_state)

    while win == False and draw == False:
        print(turn, 'to move.') 

        move = input('Where would you like to place? (1-9): ')

        if len(move) == 1 and move.isnumeric() and move != '0':
            if board_state[move] == ' ':
                board_state[move] = turn
                count += 1
            else:
                print('That space is already filled.')
                print_board(board_state)
                continue
        else:
            print('Invalid input.')
            print_board(board_state)
            continue

        print_board(board_state)

        # check for wins turn 5 and after
        if count >= 5:
            if board_state['7'] == board_state['8'] == board_state['9'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['4'] == board_state['5'] == board_state['6'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['1'] == board_state['2'] == board_state['3'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['7'] == board_state['4'] == board_state['1'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['8'] == board_state['5'] == board_state['2'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['9'] == board_state['6'] == board_state['3'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['7'] == board_state['5'] == board_state['3'] != ' ':
                print(turn, 'won.')
                win = True
            elif board_state['9'] == board_state['5'] == board_state['1'] != ' ':
                print(turn, 'won.')
                win = True

        # If nobody has won and the board is full, it's a draw
        if count == 9 and win == False:
            print("It's a draw.")
            draw = True
        
        # change the player after every move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # give option to start a new game
    new_game = input('Would you like to play again? (y/n): ').upper()
    if new_game == 'Y':
        # use the list of keys from earlier in the code to remove the X's and O's and recreate an empty board
        for key in board_keys:
            board_state[key] = ' '
        play_game()
    else:
        quit()



if __name__ == '__main__':
    play_game()
        