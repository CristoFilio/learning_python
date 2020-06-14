import random


def game():
    player_list = select_marker()
    play_game = game_start(player_list)
    moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turns = 0

    while play_game:

        for player in player_list:
            display_board(moves)
            player_move = input('{} make your move!: '.format(player[0]))
            while player_move not in moves and \
                    player_move == 'X' and player_move == 'O':
                player_move = input(
                    '{} pick an available number on the board!: '
                    .format(player[0]))

            moves[int(player_move) - 1] = player[1].upper()
            turns += 1

            if check_win(moves, player[1].upper()):
                display_board(moves)
                choice = input('{} won the game!\nDo you want to play again? yes or no: '
                               .format(player[0])).lower()
                play_game = play_again(choice)
                break
            if turns == 9:
                choice = input('Out of available moves Play again? : yes or no')
                play_game = play_again(choice)
                break
    print('Game was closed')


def select_marker():
    player_one = input('Welcome to Tic Tac Toe!\n'
                       'Player One do you want to be X or O? ')
    while player_one.lower() != 'x' and player_one.lower() != 'o':  # Check if marker is either x or o
        player_one = input('Player One choose either X or O ')  # New message asking for correct input.
    else:
        if player_one.lower() == 'x':
            player_one = 'Player One', 'x'
            player_two = 'Player Two', 'o'
        else:
            player_one = 'Player One', 'o'
            player_two = 'Player Two', 'x'
    print('Player One chose {} Player Two was assigned {}'
          .format(player_one[1].upper(), player_two[1].upper()))
    player_list = [player_one, player_two]
    random.shuffle(player_list)
    return player_list


def game_start(player_list):
    start = input(
        '{} will go first, are you ready to start? Yes or No '
            .format(player_list[0][0]))

    while start.lower() != 'yes' and start.lower() != 'no':  # Loop checks for correct input.
        start = input('Are you ready to start? Yes or No ')

    if start.lower() == 'yes':
        return True

    return False


def display_board(move):
    frame = [' ___________\n', '|   |   |   |\n', '| ', ' | ', ' |\n']

    board = ([frame[0],
              frame[1],
              frame[2], move[0], frame[3], move[1], frame[3], move[2], frame[4], frame[5],
              frame[1],
              frame[2], move[3], frame[3], move[4], frame[3], move[5], frame[4], frame[5],
              frame[1],
              frame[2], move[6], frame[3], move[7], frame[3], move[8], frame[4], frame[5]])

    print(''.join(map(str, board)))


def check_win(move, current_marker):
    if ((move[0] == move[1] == move[2] == current_marker) or
            (move[3] == move[4] == move[5] == current_marker) or
            (move[6] == move[7] == move[8] == current_marker) or
            (move[0] == move[3] == move[6] == current_marker) or
            (move[1] == move[4] == move[7] == current_marker) or
            (move[2] == move[5] == move[8] == current_marker) or
            (move[6] == move[4] == move[2] == current_marker) or
            (move[0] == move[4] == move[8] == current_marker)):
        return True
    return False


def play_again(choice):
    while choice != 'yes' and choice != 'no':
        choice = input('Do you want to play again? yes or no: ').lower()
    if choice == 'yes':
        game()
    return False


if __name__ == '__main__':
    game()
