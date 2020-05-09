"""
This is my second project. Over commenting was done for learning purposes.

This is a BlackJack game.
Features:
It can be played by multiple players.
A game table is created once the number of players has been decided.
Base funds of $1000 are assigned to every player on creation.
A minimum bet of $250 is required to play a round. Players can change their bet amount before each round.
When the players do not have the minimum bet amount they will be taken out of the game.
The game keeps track of the funds, wins, losses, and profits made.
The game play is like a regular BlackJack game.
Once a round is over players can decide to keep playing the current game table or not.
The game is able to continue while there are still players with funds and players in the game table.
The players currently on the game can decide to start a new game table, continue the current one or close the game.
The game closes when there are no remaining players.

Future Version:
Will revise winning conditions and define functions to shorten the code.
"""

import random
import string


class PlayerClass:
    """
    This class is used to create each player and keep track of their wins, loses, funds, cards, status,
    check for winning/losing conditions, draw cards
    """

    def __init__(self, player, funds=1000, status='in', game_status='pturn', holder='player', bet_made=0,
                 game_profits=0, cardtotal=0, cards='', win_count=0, lost_count=0, profits=0):

        self.player = player
        self.game_status = game_status
        self.funds = funds
        self.bet_made = bet_made
        self.status = status
        self.holder = holder
        self.cards = cards
        self.win_count = win_count
        self.lost_count = lost_count
        self.profits = profits
        self.game_profits = game_profits
        self.cardtotal = cardtotal

    def gamereset(self):  # Used to reset player cards and card total after each round.

        self.cards = ''
        self.cardtotal = 0

    def pstatus(self, statusupdate):  # Updates the status of a player, IN, OUT, Busted will be used

        self.status = statusupdate

        return self.status

    def pcards(self, action='stay'):

        """
        This is used to give a card from the top of the deck to the players. It is used during the
        initial draw phase, and during the game while asking the players if they want to stay or draw.
        It also checks the card value and checks card total.
        """

        if action == 'stay':
            pass

        elif action == 'draw':

            card = deck[0]  # Stores the value of the first card on the deck list.
            card_value = 0
            cards = [deck.pop(0)]

            self.cards = self.cards + str(cards)

            values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
            # Dictionary with keywords and values to be assigned to cards.

            for keyword in values:  # This loop checks the value of the card after it was drawn.

                if keyword in card:  # if they keyword is in the string object example: '5' in '5 of clubs'.

                    card_value = values[keyword]  # set card value to the value of the keyword.
                    break
                elif keyword not in card:  # Ff keyword not in card set card value to 10
                    card_value = 10  # Gives value of 10 to K Q J and 10.

            if card_value == 11:  # Sets the value of an Ace to 1 if the initial assigned value
                # of 11 makes the total card value over 21.

                if (self.cardtotal + card_value) > 21:
                    card_value = 1

            self.cardtotal = self.cardtotal + card_value  # Adds each card value to the card total.

            if self.cardtotal > 21:  # Checks the card total

                if self.player == 'Dealer':

                    pass

                else:  # if the player card total is over 21, then set the status to bust
                    # and substract the bet made from the funds and profits.

                    self.game_profits = self.game_profits - int(self.bet_made)
                    self.funds -= int(self.bet_made)
                    self.status = 'BUST'
                    print(f'Bad luck {self.player} your card total is {self.cardtotal} and went over 21!')
                    print('YOU LOST THIS ROUND =(\n\n')

    def pholder(self, holder):
        # used as player number holder for printing information.
        self.holder = holder
        return self.holder

    def pmakebet(self):  # this method substracts from funds each time a bet is made

        self.bet_made = 250  # set minimum bet to 250
        print(
            f'{self.player} the minimum bet amount is $250 do you wish to increase it? Your current funds are {self.funds}')

        newbet = input('Please enter new amount or type no if you wish to keep the minimum bet')

        while newbet != 'no':

            '''This while loop checks for the newbet input to be either no or a number higher than 250'''

            if newbet[0] in string.ascii_letters:
                newbet = input('Please enter new amount higher than $250 or type no')
                continue

            if int(newbet) > 250:

                while int(newbet) > self.funds:

                    print(
                        f'{self.player} you cannot bet more than what you have available! Your current funds are {self.funds}')
                    newbet = input(f'Please enter new amount between $250 and {self.funds} or type no')

                    if newbet[0] in string.ascii_letters:

                        if newbet == 'no':
                            break

                        continue

                else:

                    self.bet_made = int(newbet)
                    self.funds = self.funds - int(self.bet_made)
                    break

            if newbet == 'no':
                break

            while int(newbet) < 250:

                newbet = input('Please enter new amount higher than $250 or type no')

                if newbet == 'no':
                    break

        if newbet == 'no':
            self.bet_made = 250
            self.funds = self.funds - int(self.bet_made)

    def check_game(self):  # this method adds funds to the player according to the winning condition

        if self.status == 'in':

            if self.cardtotal > dealertotal:

                if self.cardtotal == 21:

                    '''
                    Adds a win count.
                    Player won by BlackJack and gets a higher pay.
                    '''

                    self.win_count += 1
                    self.profits = (self.bet_made * 2.5)
                    self.game_profits = self.game_profits + int(self.bet_made)
                    self.funds = self.funds + self.profits
                    print(
                        f'{self.player} Congratulations On Your Victory! \n You get extra GAINS for getting a BlackJack Your New Balance is {self.funds}')

                else:
                    '''
                    Player won by having a higher total than the dealer
                    Regular pay out and +1 win count
                    '''

                    self.win_count += 1
                    self.profits = (self.bet_made * 2)
                    self.game_profits = self.game_profits + int(self.bet_made)
                    self.funds = self.funds + self.profits
                    print(f'{self.player} Congratulations On Your Victory! \n Your New Balance is {self.funds}')

                play_again = input(f'{self.player} do you wish to play again? yes or no')

                '''
                Asks the player if the want to play again.
                Set player status to in or out
                '''

                while play_again != 'yes' and play_again != 'no':
                    play_again = input('Do you wish to play again? yes or no')
                if play_again == 'yes':
                    self.status = 'in'
                else:
                    self.status = 'out'


            elif self.cardtotal < dealertotal:

                '''
                If the player total is less than the dealer total, but the dealer total is greater than 21 and busted.
                check if the player has a blackjack and add funds and a win count.
                Add funds for a regular win.
                '''

                if dealertotal > 21:

                    if self.cardtotal == 21:

                        self.win_count += 1
                        self.profits = (self.bet_made * 2.5)
                        self.game_profits = self.game_profits + int(self.bet_made)
                        self.funds = self.funds + self.profits
                        print(
                            f'{self.player} Congratulations On Your Victory! \n '
                            f'You get extra GAINS for getting a BlackJack Your New Balance is {self.funds}')

                    else:

                        self.win_count += 1
                        self.profits = (self.bet_made * 2)
                        self.game_profits = self.game_profits + int(self.bet_made)
                        self.funds = self.funds + self.profits
                        print(f'{self.player} Congratulations On Your Victory! \nYour New Balance is {self.funds}')

                        play_again = input(f'{self.player} do you wish to play again? yes or no')

                        while play_again != 'yes' and play_again != 'no':
                            play_again = input('Do you wish to play again? yes or no')

                        if play_again == 'yes':
                            self.status = 'in'
                        else:
                            self.status = 'out'

                else:
                    ''' 
                    If the dealer did not bust and the dealer total is greater than the player.
                    Subtract the bet made from the funds and the profits and add a loss to the player.
                    '''
                    self.game_profits = self.game_profits - int(self.bet_made)

                    if self.funds < 250:
                        # player does not have enough funds and is set to out
                        self.lost_count += 1
                        self.status = 'out'
                        print(f'{self.player} you do not have enough funds to keep playing better luck next time')

                    else:
                        # add a loss to the player
                        self.lost_count += 1

                        play_again = input(f'{self.player} You Lost this game do you wish to play again? yes or no')

                        while play_again != 'yes' and play_again != 'no':
                            play_again = input(f'{self.player} You Lost this game do you wish to play again? yes or no')
                        if play_again == 'yes':
                            self.status = 'in'
                        else:
                            self.status = 'out'





            elif self.cardtotal == dealertotal:

                """
                The player tied with the dealer.
                Return bet made and ask if they want to play again
                """

                self.funds = self.funds + int(self.bet_made)

                print(f'{self.player} You had a tie with the dealer and you get your bet back {self.funds}')

                play_again = input(f'{self.player} You had a tie with the dealer, do you wish to play again? yes or no')

                while play_again != 'yes' and play_again != 'no':
                    play_again = input('Do you wish to play again? yes or no')
                if play_again == 'yes':
                    self.status = 'in'
                else:
                    self.status = 'out'

        elif self.status == 'BUST':

            if self.player == "Dealer":
                self.status = 'dealer'

            else:

                self.lost_count += 1
                self.game_profits = self.game_profits - int(self.bet_made)
                if self.funds < 250:
                    self.status = 'out'
                    print(f'{self.player} you do not have enough funds to keep playing better luck next time')

                else:
                    self.lost_count += 1
                    self.game_profits = self.game_profits - int(self.bet_made)

                    play_again = input(f'{self.player} You Lost this game by BUST do you wish to play again? yes or no')

                    while play_again != 'yes' and play_again != 'no':
                        play_again = input(
                            f'{self.player} You Lost this game by BUST do you wish to play again? yes or no')
                    if play_again == 'yes':
                        self.status = 'in'
                    else:
                        self.status = 'out'

    def __str__(self):  # prints information about the player

        if self.player == 'Dealer':
            if self.game_status == 'pturn':
                return (f'{self.player} cards : {self.cards}, Hidden Card - Card Total: {self.cardtotal}')
            elif self.game_status == 'dturn':
                return (f'{self.player} cards: {self.cards} Card Total: {self.cardtotal}')

        else:
            return (
                f'{self.holder}: {self.player} Balance: {self.funds} Won: {self.win_count} Lost: {self.lost_count} Profits: {self.game_profits}\nCurrent Bet : {self.bet_made}\nCards in play: {self.cards} = {self.cardtotal}\nStatus {self.status}')


# create shuffle deck

def deck_shuffle():  # Takes one object as input in this case list deck

    global deck
    '''
    This functions creates and shuffles the deck by grabing each card in
    the deck at random and putting it at the end of the deck
    '''
    numbers_symbols = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
                       'King']  # numbers and symbols used for cards
    clubs = [x + ' of Clubs' for x in
             numbers_symbols]  # Creates a list of clubs cards using the numbers and symbols list
    hearts = [x + ' of Hearts' for x in
              numbers_symbols]  # Creates a list of hearts cards using the numbers and symbols list
    spades = [x + ' of Spades' for x in
              numbers_symbols]  # Creates a list of spades cards using the numbers and symbols list
    diamonds = [x + ' of Diamonds' for x in
                numbers_symbols]  # Creates a list of diamonds cards using the numbers and symbols list

    deck = clubs + hearts + spades + diamonds  # Creates the deck using all the card lists created above

    random.shuffle(deck)
    return deck


# create players

def num_of_players():
    players = input('Welcome to BlackJack, how many guests will be playing? ')

    playernumbers = ['1', '2', '3', '4', '5']

    while players not in playernumbers:
        players = input('Please use a number to enter a maximum of five players? ')
        print(players)
    players = range(int(players))
    return players


def player_creator():
    """
    This function creates the players depending on the playernumber set on the previous function
    It is basically turning the players from False to True
    """

    global playerlist

    players = num_of_players()  # takes number from num of players

    playerlist = [False, False, False, False, False, ]  # default five max players set to false

    for x in players:  # changes playerlist to True depending on players variable
        playerlist[x] = True

    if playerlist[0] == True:
        player1 = PlayerClass(input('Player one enter your name'))  # creates an instance of the class if player is on
        player1.pholder('Player One')  # just a holder for the display board
    else:
        player1 = PlayerClass('not playing', 0, 'out')

    if playerlist[1] == True:
        player2 = PlayerClass(input('Player two enter your name'))
        player2.pholder('Player Two')
    else:
        player2 = PlayerClass('not playing', 0, 'out')

    if playerlist[2] == True:
        player3 = PlayerClass(input('Player three enter your name'))
        player3.pholder('Player Three')
    else:
        player3 = PlayerClass('not playing', 0, 'out')

    if playerlist[3] == True:
        player4 = PlayerClass(input('Player four enter your name'))
        player4.pholder('Player Four')
    else:
        player4 = PlayerClass('not playing', 0, 'out')

    if playerlist[4] == True:
        player5 = PlayerClass(input('Player five enter your name'))
        player5.pholder('Player Five')
    else:
        player5 = PlayerClass('not playing', 0, 'out')

    dealer = PlayerClass('Dealer', 0, 'dealer')  # creates dealer

    playerlist = [player1, player2, player3, player4, player5, dealer]
    # list of player classes
    return playerlist


playerlist = []
deck = []
dealertotal = 0


def gamestart():
    startgame = input('Are you ready to start the game?')
    while startgame != 'yes' and startgame != 'no':
        startgame = input('Are you ready to start the game?')

    return startgame


def gameplay():
    global deck
    global dealertotal
    # global playerlist

    playerlist = player_creator()
    startgame = gamestart()

    while startgame != 'no':

        deck = deck_shuffle()

        if (playerlist[0].status == playerlist[1].status == playerlist[2].status == playerlist[3].status == playerlist[
            4].status == 'out'):
            # if all the player status are out end the game

            print('No players remaining or with enough funds to continue playing, Game was closed')
            break

        for x in playerlist:  # reset game and ask for bet change if player is in

            if x.status == 'in':

                x.gamereset()
                x.pmakebet()

            else:
                pass

        for x in playerlist:  # draw phase

            if x.status == 'in':  # players draw

                x.pcards('draw')

                x.pcards('draw')

                print(x)
                print('\n')

            elif x.status == 'dealer':  # dealer draws and keeps one card hidden

                x.pcards('draw')
                print(x)
                print('\n')
                x.pcards('draw')
            else:
                pass

        for x in playerlist:  # ask if players want to draw again

            while x.status == 'in':

                hit = input(
                    f'{x.player} Your current total is: {x.cardtotal} Do you want to draw again? Type stay or draw')

                while hit != 'stay' and hit != 'draw':
                    hit = input(
                        f'{x.player} Your current total is: {x.cardtotal} Do you want to draw again? Type stay or draw')

                if hit == 'stay':
                    break
                print('\n')
                x.pcards(hit)
                print(x)

            if x.status == 'dealer':

                x.gamestatus = 'dturn'
                pause = input('It is now the Dealers turn to draw')
                print(x)

                while x.cardtotal < 17:
                    x.pcards('draw')
                    print(x)
                    if x.cardtotal > 21:
                        dealertotal = x.cardtotal
                        x.status = 'BUST'
                        print(f'{x.player} has BUSTED,\nEVERYONE NOT BUSTED WINS!')

                else:

                    dealertotal = x.cardtotal

        for x in playerlist:
            x.check_game()

        playagain = input(f'Continue or new game? You can also type close to end the game')

        while playagain != 'continue' and playagain != 'new game' and playagain != 'close':
            playagain = input(f'Continue or new game? You can also type close to end the game')

        if playagain == 'continue':

            for x in playerlist:
                x.gamereset()

            continue

        elif playagain == 'new game':

            gameplay()

        elif playagain == 'close':
            startgame = 'no'

    else:

        print('Game was closed')


gameplay()
