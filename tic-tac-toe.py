'''

This is my first project I created while learning the basics.
I used Jupiter notebook to create it.
I overcommented this project to help myself during the learning process.


This is a game of tic tac toe.
This game has five functions.
selectmarker - Requests player one to chose x or o, then assigns the other marker to player 2.
gamestart - Randomly picks what player will go first and asks if players are ready to play.
displayboard - Creates the board by using two lists. One list contains the frame of the board and the other list contains
               the index location for the frame list objects and the index location for the number list which contains
               the playable board slots to be modified as the game is played.
checkwin - Contains a list of index locations in the number list which represent winning conditions
           which are compared to the player assigned marker.
game - Contains the loops for the game and for each player turn.

'''


from IPython.display import clear_output  # Imports clear output module used to clear and refresh the board after each input.
import random  # Imports random module to randomize what player goes first.


def selectmarker():  # Ask player one to select their marker.

    player1 = input('Welcome to Tic Tac Toe!\nPlayer One do you want to be X or O? ')  # Initial welcome message.

    while player1.lower() != 'x' and player1.lower() != 'o':  # Check if marker is either x or o
        clear_output()
        player1 = input('Player One choose either X or O ')  # New message asking for correct input.

    else:
        if player1.lower() == 'x':  # Assign a marker to each player variable.

            player2 = 'o'

        else:
            player2 = 'x'

    clear_output()  # Clears screen and prints assigned markers.
    print(f'Player One chose {player1.upper()} Player Two was assigned {player2.upper()}')

    return player1, player2  # Returns the player variables with their assigned value.


def gamestart():  # Ask if the players are ready to play.

    rand = random.randint(0, 1)  # Create a random number between 0 and 1 and assign to variable.

    if rand == 0:  # If random number is 0, first turn "playerturn" is for player one, else it is for player two.
        playerturn = 'One'
    else:
        playerturn = 'Two'

    start = input(
        f'Player {playerturn} will go first, are you ready to start? Yes or No ')  # Display what player goes first and
    # ask if players are ready to play.
    while start.lower() != 'yes' and start.lower() != 'no':  # Loop checks for correct input.

        start = input('Are you ready to start? Yes or No ')

    else:  # Sets playgame variable to true or false based on input.
        if start.lower() == 'yes':
            playgame = True

        elif start.lower() == 'no':

            playgame = False

    return playgame, playerturn  # Returns varibales playgame and playerturn with their assigned value.


def game():  # Starts game.

    player1, player2 = selectmarker()  # Grab player1 and player 2 variable from previous function.
    playgame, playerturn = gamestart()  # Grab playerturn and playgame variables from previous funtion.

    currentplayer = ''  # Create empty variable to be used to check for winner depending on the marker that the player has.

    def display_board(num):  # Create board.

        fr = [' ___________\n', '|   |   |   |\n', '| ', ' | ', ' |\n',
              '|___|___|___|\n']  # List of strings that form the frame.

        board = ([fr[0], fr[1], fr[2], num[0], fr[3], num[1], fr[3], num[2],
                  # List with index locations to fr list and number list objects.
                  fr[4], fr[5], fr[1], fr[2], num[3], fr[3], num[4], fr[3], num[5],
                  fr[4], fr[5], fr[1], fr[2], num[6], fr[3], num[7], fr[3], num[8], fr[4], fr[5]])

        clear_output()  # Resets the board after each turn is player.
        print(''.join(map(str,
                          board)))  # Prints the updated board using the join function and turning the board list into strings.

    def checkwin(numbers, currentplayer):  # Check for winning condition to be true.
        if ((numbers[0] == numbers[1] == numbers[
            2] == currentplayer) or  # There are eight ways to win, three rows, three columns
                (numbers[3] == numbers[4] == numbers[5] == currentplayer) or  # and two across.
                (numbers[6] == numbers[7] == numbers[
                    8] == currentplayer) or  # This checks each number based on their index location.
                (numbers[0] == numbers[3] == numbers[
                    6] == currentplayer) or  # Each row in this function is an index combination that
                (numbers[1] == numbers[4] == numbers[7] == currentplayer) or  # would result into a win.
                (numbers[2] == numbers[5] == numbers[
                    8] == currentplayer) or  # Currentplayer holds the marker assigned to each player
                (numbers[6] == numbers[4] == numbers[2] == currentplayer) or  # and its compared to the indexed numbers.
                (numbers[0] == numbers[4] == numbers[
                    8] == currentplayer)):  # If any of the conditions are True, set game over to True
            gameover = True
        else:
            gameover = False  # This allows the game to continue.

        return gameover  # Returns the variable gameover and its value.

    numbers = [1, 2, 3, 4, 5, 6, 7, 8,
               9]  # List holds the values of the board slots and gets modified by player input using the assigned marker.

    gameover = False  # Initial value.

    turns = 0  # Counts the turns, there should only be 9 playable turns. Used to stop the game at max turns.
    player_move = 0  # Hold the player input to be checked or placed in board.

    if playgame == False:  # Terminates game if player is not ready.
        return 'Game Has Been Terminated'

    else:  # Starts the game.

        display_board(numbers)  # Prints the board using the displayboard function
        # and the numbers list as input to the display board function.

        while gameover != True:  # If gameover is not true start the game loop.

            if turns == 9:  # Checks for maximum number of turns.
                gameover = True  # Causes the game while loop to close.

            while playerturn == 'One':  # This starts the player 1 loop turn.
                currentplayer = player1.upper()  # Sets current player to the marker the player selected before.

                player_move = int(input('Player One make your move!'))  # Request player for input.

                while player_move not in numbers:  # While loop to check if the input is available in the numbers list.

                    player_move = int(
                        input('Player One pick an available number on the board'))  # Request available input.

                if player_move in numbers:  # If the input is on the number list.

                    numbers[(
                                player_move) - 1] = player1.upper()  # Change the number in the number list to the assigned player marker
                    # by using index location.
                    # (player_move)-1 represents the index location of the input.
                    # Exapmple: number 1 on the list is index 0, so input 1 -1 = 0

                    turns += 1  # Add a turn to turn counter.

                if checkwin(numbers,
                            currentplayer) == True:  # Calls the checkwin function using the modified numbers list and
                    # currentplayer assigned marker.

                    display_board(numbers)  # Display board with winning play.
                    winner = "One"  # Used to hold value of what player won the game.
                    gameover = True  # Set gameover to false which ends the game loop.
                    break  # Breaks the loop.

                else:  # If no winning condition is found.

                    display_board(numbers)  # Display board with current play.
                    playerturn = 'Two'  # Set playerturn to two which ends the player one loop.

            while playerturn == 'Two':  # Starts player2 turn loop.
                currentplayer = player2.upper()  # Sets current player to the marker the player selected before.

                player_move = int(input('Player Two make your move!'))  # Request player for input.

                while player_move not in numbers:  # While loop to check if the input is available in the numbers list.

                    player_move = int(
                        input('Player Two pick an available number on the board'))  # Request available input.

                if player_move in numbers:  # If the input is on the number list.

                    numbers[(
                                player_move) - 1] = player2.upper()  # change the number in the number list to the assigned player marker
                    # by using index location
                    # (player_move)-1 represents the index location of the input
                    # Exapmple: number 1 on the list is index 0, so input 1 -1 = 0

                    turns += 1  # Add a turn to turn counter.

                if checkwin(numbers,
                            currentplayer) == True:  # Calls the checkwin function using the modified numbers list and
                    # currentplayer assigned marker.

                    display_board(numbers)  # Display board with winning play.
                    winner = "Two"  # Used to hold value of what player won the game.
                    gameover = True  # Set gameover to false which ends the game loop.
                    break  # Breaks the loop.

                else:  # If no winning condition is found.

                    display_board(numbers)  # Display board with current play.
                    playerturn = 'One'  # Set playerturn to one which ends the player two loop.

        else:  # This executes if the game loop is broken by the gameover variable.

            replay = input(
                f'Player {winner} Won!, do you want to play again?')  # Ask player if they wish to play again.

            while replay.lower() != 'yes' and replay.lower() != 'no':  # While loop to check for yes or no.

                replay = input('Do you want to play again? Yes or No')  # Request correct input.

            else:  # Runs after player has provided a yes or no answer.

                if replay == 'yes':
                    clear_output()  # Clears the screen.
                    game()  # Starts the game function again.

                elif replay == 'no':
                    clear_output()  # Clears the screen.
                    print('Thank you for playing!')  # Thanks the player.


game()
