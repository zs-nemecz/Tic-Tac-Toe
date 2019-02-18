### Missing functions
# - save win history

import time
import random
key_number = {'7':0,'8':1, '9':2,'4':3,'5': 4,'6':5,'1':6, '2':7, '3':8}
winning_combos = [[0,1,2],[3,4,5],[6,7,8],[6,3,0],[7,4,1],[8,5,2],[0,4,8],[6,4,2]]
player1 = {'name':'Player 1', 'moves': [], 'wins': 0, 'marker': '| x |'}
player2 = {'name':'Player 2', 'moves': [], 'wins': 0, 'marker': '| o |'}
accepted_input = ('p', 'n', 'h', 'q', 'm')
board = ['|   |'] * 9
players = [player1, player2]

################################################################################################################

def display_board(board):
    print('-----------------')
    for i,symbol in enumerate(board):
        if i == 0 or i == 3 or i == 6:
            print('|', end="")

        print(symbol, end="")

        if i == 2 or i == 5 or i == 8:
            print('|')
            print('-----------------')

################################################################################################################

def new_board():
    return ['|   |'] * 9

################################################################################################################

def take_input(player):
    print('{}\'s turn'.format(players[player -1]['name']))
    input_accepted = False
    while (not input_accepted):
        move = input('Your move:\n')
        if (move in key_number.keys()):
            if board[key_number[move]] != '|   |':
                print('\n'*50)
                display_board(board)
                print('Position already occupied. Try again!')
                time.sleep(0.5)
            else:
                input_accepted = True
                return move
        elif(move in accepted_input):
            input_accepted = True
            return move
        else:
            print('\n'*50)
            display_board(board)
            print('Unknown option. Please try again!')
            print('Press {} for moves, or h for Help and q to Quit.'.format(list(key_number.keys())))

################################################################################################################

def update_board(player):
    return players[player - 1]['marker']

################################################################################################################

def register_move(player, move):
    players[player - 1]['moves'].append(key_number[move])

################################################################################################################

def check_win(players, player, winning_combos):
    for i in winning_combos:
        result = all(elem in (players[player - 1]['moves']) for elem in i)
        if result:
            print('Yay!!!{} won!'.format(players[player - 1]['name']))
            players[player - 1]['wins'] += 1
            return True
    else:
        return False

################################################################################################################

def check_draw(player1):
    draw = len(player1['moves']) >= 5
    if draw:
        print('It\'s a draw!')
    return draw

################################################################################################################

def replay_game():
    answer = input('Do you want to play again? y/n?\n')
    return (answer.lower() == 'y') or (answer.lower() == 'yes')

################################################################################################################

def print_help():
    h = None
    help_board = ['| 7 |',  '| 8 |',  '| 9 |', '| 4 |','| 5 |', '| 6 |','| 1 |','| 2 |','| 3 |']
    demo_board = new_board()
    demo_board[key_number['5']] = update_board(1)
    while (h == None):
        print('\n'*50)
        print('Press p to start the game.')
        print('When the game is on, enter a digit to select the location to place your marker.')
        display_board(help_board)
        print('\nAfter entering 5 for example, the board will look like this:')
        display_board(demo_board)
        print('\nThe player who has 3 markers in a row, column or diagonal, wins.')
        demo_board[key_number['1']] = update_board(1)
        demo_board[key_number['9']] = update_board(1)
        display_board(demo_board)
        h = input('Press Enter key to continue...')

################################################################################################################

def game_on():
    ongoing_game = True
    player = random.choice([1,2])
    print('\n'*50)
    display_board(board)
    while (ongoing_game):
        if player == 1:
            player = 2
        else:
            player = 1
        move = take_input(player)
        while move in accepted_input:
            if move == 'h':
                while move == 'h':
                    print_help()
                    display_board(board)
                    move = take_input(player)
            else:
                q = input('Are you sure you want to quit this game?\nPress y/n: ')
                if q.lower() == 'y' or q.lower() == 'yes':
                    action = move
                    ongoing_game = False
                    return action
                else:
                    print('\n'*50)
                    display_board(board)
                    move = take_input(player)
        if (move in list(key_number.keys())):
            register_move(player, move)
            print(players[player-1]['moves'])
            board[key_number[move]] = update_board(player)
            print('\n'*50)
            display_board(board)
            if (check_win(players, player, winning_combos)) or (check_draw(player1)):
                ongoing_game = False
                print('\n{} has {} wins.'.format(player1['name'], player1['wins']))
                print('{} has {} wins.'.format(player2['name'], player2['wins']))
                if replay_game():
                    return 'p'
                else:
                    return 'x'

################################################################################################################

def select_option(accepted_input):
    user_input = input('Select an option:\n')
    if user_input in accepted_input:
        return user_input
    else:
        print('\n'*50)
        print('Unknown option. Please select again!')
        time.sleep(1.2)
        return 'x'

################################################################################################################

def assign_marker(players):
    mx = '| x |'
    mo = '| o |'
    print('{}, which marker do you want to play with?'.format(players[0]['name']))
    marker = ''
    while (not(marker.lower() in ['x', 'o'])):
        marker = input('Select \'x\' or \'o\':')

    if marker.lower() == 'x':
        players[0]['marker'] = mx
        players[1]['marker'] = mo
    else:
        players[0]['marker'] = mo
        players[1]['marker'] = mx

################################################################################################################

def assign_names(players):
    name = None
    for i in [1,2]:
        name = input(f'Set name for Player {i}:')
        if len(name) > 0:
            players[i-1]['name'] = name

################################################################################################################

def quit_game():
    q = input('Are you sure you want to exit?\nPress y/n: ')
    if q.lower() == 'y' or q.lower() == 'yes':
        print('\n'*50)
        print('Goodbye')
        time.sleep(0.5)
        return False
    else:
        print('\n'*50)
        return True

################################################################################################################
################################################################################################################
################################################################################################################

print('\n'*50)
print('              Hello Players!')
print('\n'*10)
time.sleep(0.5)
print('\n'*50)
print('************This Is TiC TaC ToE!***************')
print('\n'*10)
time.sleep(0.5)

menu = True
while(menu):
    players[0]['wins'] = 0
    players[1]['wins'] = 0
    action = 'x'
    print('\n'*50)
    print('OPTIONS\n[p] - Play\n[n] - Add Names\n[h] - Select marker: x/o\n[q] - Help\n[m] - Quit')
    action = select_option(accepted_input)
    while(action == 'p'):
        board = new_board()
        players[0]['moves'] = []
        players[1]['moves'] = []
        action = game_on()
        if action != 'p':
            if (player1['wins'] > player2['wins']):
                print('{} WON!'.format(player1['name'].upper()))
            elif(player1['wins'] < player2['wins']):
                print('{} WON!'.format(player2['name'].upper()))
            elif (player1['wins'] + player2['wins']) > 0:
                print('That\'s a draw!')
        time.sleep(1.5)
        print('\n'*50)
    if (action == 'm'):
        assign_marker(players)
    elif (action == 'n'):
        assign_names(players)
    elif (action=='h'):
        print_help()
    elif (action == 'q'):
        menu = quit_game()
