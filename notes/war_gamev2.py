import random


class PlayerCreator:

    def __init__(self, name='Computer', cards=[], total_points=0, turns_won=0):

        self.name = name
        self.cards = cards
        self.total_points = total_points
        self.turns_won = turns_won

    def play_card(self, num=1):

        played_cards = []
        while num != 0 and len(self.cards) != 0:
            played_cards += [self.cards.pop(0)]
            num -= 1
        return played_cards

    def won_turn(self, cards):

        print(self.name, 'won this turn \n')
        self.turns_won += 1
        self.total_points += card_value(cards)

        for x in cards:
            self.cards.append(x)


def deck_creator():
    symbols = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
               'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    sleeves = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
    values = [n for n in [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14] for x in range(4)]
    deck = [(x + ' of ' + y, values.pop(0)) for x in symbols for y in sleeves]
    random.shuffle(deck)
    return deck


def split_deck():
    deck = deck_creator()
    player_cards = []
    computer_cards = []
    while len(deck) != 0:
        player_cards.append(deck.pop(0))
        computer_cards.append(deck.pop(0))
    game_start(computer_cards, player_cards)


def card_value(cards):
    card_sum = 0
    for card in cards:
        card_sum += card[1]
    return card_sum


def higher_value(player_draw, computer_draw, computer, player):
    print('Player cards value: ', card_value(player_draw),
          'Computer cards value: ', card_value(computer_draw))

    if card_value(player_draw) < card_value(computer_draw):
        for x in player_draw:
            computer_draw.append(x)
        computer.won_turn(computer_draw)

    elif card_value(player_draw) > card_value(computer_draw):
        for x in computer_draw:
            player_draw.append(x)
        player.won_turn(player_draw)

    elif card_value(player_draw) == card_value(computer_draw):

        print('War goes on! Draw again to end the war.\n')
        draw = input('Press enter to draw')
        player_draw += player.play_card()
        computer_draw += computer.play_card()
        print('{} flipped a '.format(player.name), player_draw)
        print('Cards remaining :', len(player.cards), '\n')
        print('Computer flipped a ', computer_draw)
        print('Cards remaining :', len(computer.cards), '\n')
        higher_value(player_draw, computer_draw, computer, player)


def game_start(comp_cards, play_cards):
    player = PlayerCreator(name=(input('What is your name?')), cards=play_cards)
    computer = PlayerCreator(cards=comp_cards)
    turns_played = 0
    wars_fought = 0

    while len(player.cards) != 0 and len(computer.cards) != 0:

        turns_played += 1
        player_draw = player.play_card()
        computer_draw = computer.play_card()
        print('\n--- Turn {} ---'.format(turns_played))
        draw = input('Press enter to draw')
        print('{} flipped a '.format(player.name), player_draw)
        print('Cards remaining :', len(player.cards), '\n')
        print('Computer flipped a ', computer_draw)
        print('Cards remaining :', len(computer.cards), '\n')

        if card_value(player_draw) == card_value(computer_draw):

            print('Player cards value: ', card_value(player_draw),
                  'Computer cards value: ', card_value(computer_draw))
            wars_fought += 1
            print('\n --- WAR! ---\n')
            draw = input('Press enter to draw four cards')

            for x in [player.play_card(4)]:
                player_draw += x
                print('{} flipped '.format(player.name), player_draw, '')

            for x in [computer.play_card(4)]:
                computer_draw += x
                print('Computer flipped ', computer_draw, '\n')

            higher_value(player_draw, computer_draw, computer, player)
            continue

        higher_value(player_draw, computer_draw, computer, player)

    if len(player.cards) == 0:
        print('\nComputer has won the game\n')
    elif len(computer.cards) == 0:
        print('\n{} you won the game!\n'.format(player.name))

    print('Turns Played: ', turns_played)
    print('Wars Played', wars_fought)
    print('Your Points: ', player.total_points)
    print('You won a total of ', player.turns_won, 'turns')
    print('Computer Points: ', computer.total_points)
    print('Computer won a total of ', computer.turns_won, 'turns')
    print('\n--- THANK YOU FOR PLAYING! ---')


if __name__ == '__main__':
    split_deck()
