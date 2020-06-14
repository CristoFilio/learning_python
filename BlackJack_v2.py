import random

class PlayerClass:
    def __init__(self, name='', funds=1000, status='in',
                 game_status='player_turn', holder='player', bet_made=0,
                 game_profits=0, card_total=0, cards=[],
                 win_count=0, lost_count=0, profits=0):
        self.name = name
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
        self.card_total = card_total

    def game_reset(self):
        self.cards = []
        self.card_total = 0

    def p_cards(self, deck, amount=1):

        for amount in range(amount):
            card_value = deck[0][1]
            self.cards.append(deck.pop(0))

            if card_value == 11 and (self.card_total + card_value) > 21:
                card_value = 1
            self.card_total += card_value

            if self.card_total > 21 and self.name != 'Dealer':
                self.game_profits -= float(self.bet_made)
                self.lost_count += 1
                self.status = 'BUST'
                self.bet_made = 0
                print('\nBad luck {} your card total is {} and '
                      'went over 21!'.format(self.name, self.card_total))
                print('YOU LOST THIS ROUND.\n')
                keep_playing(self)

    def p_make_bet(self):
        print(
            '\n{} the minimum bet amount is $250 do you '
            'wish to increase it? Your current funds are {}'
                .format(self.name, self.funds))
        new_bet = ''
        while new_bet != 'no':
            while not new_bet.isnumeric() and new_bet !='no':
                new_bet = input('\nPlease enter new amount higher than $250 or type no :')
                continue

            if new_bet.isnumeric():
                if float(new_bet) < 250:
                    new_bet = 'try-again'
                    continue
                if float(new_bet) > self.funds:
                    print(
                        '\n{} you cannot bet more than what you '
                        'have available! Your current funds are {}'
                            .format(self.name, self.funds))
                    new_bet = 'try-again'
                    continue
                else:
                    self.bet_made = float(new_bet)
                    self.funds -= float(self.bet_made)
                    return

        if new_bet == 'no':
            self.bet_made = 250
            self.funds -= float(self.bet_made)

    def check_game(self, dealer):
        if self.status == 'in':

            if self.card_total > dealer.card_total or dealer.status == 'Busted':
                check_win(self)

            elif self.card_total == dealer.card_total:
                self.funds += float(self.bet_made)
                print('\n{} You had a tie with the dealer '
                      'and you get your bet back. Remaining Funds: {}\n'
                      .format(self.name, self.funds))
            else:
                lost_game(self)

    def __str__(self):
        if self.name == 'Dealer':
            if self.game_status == 'player_turn':
                return ('\n{} cards : {}, Hidden Card\nCard Total: {}'
                        .format(self.name, ", ".join([card[0] for card in self.cards]),
                                self.card_total))
            elif self.game_status == 'dealer_turn':
                return ('\n{} cards: {} \nCard Total: {}'
                        .format(self.name, ", ".join([card[0] for card in self.cards]),
                                self.card_total))
        else:
            return (
                '\n{}: {} | Balance: {} | Won: {} | Lost: {} | Profits: {}\n'
                    .format(self.holder, self.name, self.funds, self.win_count,
                            self.lost_count, self.game_profits)+
                'Current Bet : {} | Status: {}\nCards in play: {}\nCard Total: {}'
                    .format(self.bet_made, self.status,
                            ", ".join([card[0] for card in self.cards]), self.card_total))

def deck_shuffle():
    symbols = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
               'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    sleeves = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
    values = [n for n in [11,2,3,4,5,6,7,8,9,10,10,10,10] for x in range(4)]
    deck = [(x+' of '+y, values.pop(0))for x in symbols for y in sleeves ]
    random.shuffle(deck)
    return deck

def game_play():
    player_list = player_creator()
    start_game = game_start()

    while start_game != 'no' and player_check(player_list):
        deck = initial_draw(player_list)
        draw_again(player_list,deck)
        dealer = player_list[-1]
        for player in player_list:
            player.check_game(dealer)

        delete_player(player_list)
        start_game = play_again(player_list)
    if not player_check(player_list):
        print('No remaining players in the table.\nGame has been Terminated')
    else:
        print('Game was closed')

def game_start():
    start_game = ''
    while start_game != 'yes' and start_game != 'no':
        start_game = input('Are you ready to start the game? yes or no: ')
    return start_game

def player_creator():
    player_list = []
    players = num_of_players()
    player_number = ['Player One', 'Player Two',
                     'Player Three', 'Player Four', 'Player Five']
    for n in range(players):
        player_list.append(PlayerClass(holder=player_number.pop(0)))
        player_list[-1].name = input('\n{} please enter your name: '
                                      .format(player_list[-1].holder)).capitalize()
        player_list[-1].p_make_bet()
    dealer = PlayerClass(name='Dealer', status='dealer',
                               holder='Dealer')
    player_list.append(dealer)
    return player_list

def num_of_players():
    players = input('\nWelcome to BlackJack, how many '
                    'guests will be playing? up to five: ')
    while not players.isdigit() or players not in '12345':
        players = input('\nPlease use a number to '
                        'enter a maximum of five players:  ')
    return int(players)

def player_check(player_list):
    for player in player_list:
        if player.status == 'in':
            return True
    return False

def initial_draw(player_list):
    deck = deck_shuffle()
    for player in player_list:
        player.game_reset()
        if player.status == 'dealer':
            player.p_cards(deck)
            print(player, '\n')
            player.p_cards(deck)
        else:
            player.p_cards(deck,2)
            print(player)
    return deck

def draw_again(player_list,deck):
    for player in player_list:
        while player.status == 'in':
            hit = ''
            while hit != 'stay' and hit != 'draw':
                hit = input(
                    '\n{} Your current total is: {} Do you want to draw again?'
                    ' Type stay or draw :'.format(player.name, player.card_total))
            if hit == 'stay':
                break
            else:
                player.p_cards(deck)
                print(player)
        if player.status == 'dealer':
            pause = input('\nIt is now the Dealers turn to draw')
            player.game_status = 'dealer_turn'
            print(player)
            while player.card_total < 17:
                player.p_cards(deck)
                print(player)
                if player.card_total > 21:
                    player.status = 'Busted'
                    print('\n{} has BUSTED,\nEVERYONE NOT BUSTED WINS!'.format(player.name))

def lost_game(player):
    player.game_profits -= float(player.bet_made)
    player.lost_count += 1
    print('\n{} You lost this game. '
          'Your New Balance is {}'.format(player.name, player.funds))
    keep_playing(player)

def check_win(player):
    if player.card_total == 21:
        black_jack(player)
    else:
        regular_win(player)

def regular_win(player):
    player.win_count += 1
    player.profits = (player.bet_made * 2)
    player.game_profits = player.game_profits + float(player.bet_made)
    player.funds = player.funds + player.profits
    print('\n{} Congratulations On Your Victory! \n'
          'Your New Balance is {}'.format(player.name, player.funds))
    keep_playing(player)

def black_jack(player):
    player.win_count += 1
    player.profits = (player.bet_made * 2.5)
    player.game_profits = player.game_profits + float(player.bet_made)
    player.funds = player.funds + player.profits
    print(
        '\n{} Congratulations On Your Victory! \n '
            .format(player.name),
        'You get extra GAINS for getting a BlackJack '
        'Your New Balance is {}'.format(player.funds))
    keep_playing(player)

def keep_playing(player):
    choice = ''
    while choice != 'yes' and choice != 'no':
        choice = input('{} do you wish to keep playing? yes or no :'.format(player.name))
    if choice == 'no':
        player.status = 'out'
        return
    check_funds(player)

def check_funds(player):
    if player.funds < 250:
        player.status = 'out'
        print('{} you do not have enough funds to '
              'keep playing better luck next time\n'.format(player.name))

def delete_player(player_list):
    player_list[-1].status = 'dealer'
    for player in player_list:
        if player.status == 'out':
            player_list.remove(player)
        if player.status == 'BUST':
            player.status = 'in'

def play_again(player_list):
    choice = ''
    while choice != 'continue' and choice != 'new game' and choice != 'close':
        choice = input('Please type continue, new game, or close :').lower()

    if choice == 'continue':
        for player in player_list:
            player.game_reset()
            if player.status == 'in':
                player.p_make_bet()
        return
    elif choice == 'new game':
        game_play()
    elif choice == 'close':
        start_game = 'no'
        return start_game

if __name__ == '__main__':
    game_play()