#! /usr/bin/env python3

# 独学プログラマー チャレンジ問題15.0
# 2019/01/15更新
# 2019/01/11初出

# 「戦争」ゲームを自分で一から書いてみる

from random import shuffle

class Card:
    suites = ('spade', 'heart', 'diamond', 'club')
    values = (None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, s, v):
        self.suite = s
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suite < c2.suite:
                return True
        else:
            return False

    def __repr__(self):
        return '{} of {}'.format(self.values[self.value], self.suites[self.suite])

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 4):
            for j in range(2, 14):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

'''
deck = Deck()
while len(deck.cards) > 0:
    print(deck.cards.pop())
'''

class Player:
    def __init__(self, n):
        self.name = n
        self.card = []
        self.wins = 0

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player('player1')
        self.player2 = Player('player2')

    def play(self):
        print('\nLet the card war game begin.')
        while len(self.deck.cards) >= 2:
            print('\n{} cards on deck'.format(len(self.deck.cards)))

            self.player1.card = self.deck.cards.pop()
            self.player2.card = self.deck.cards.pop()

            print('Player1: {}'.format(self.player1.card))
            print('Player2: {}'.format(self.player2.card))

            if self.player1.card < self.player2.card:
                print('Player2 wins.')
                self.player2.wins += 1
            else:
                print('Player1 wins.')
                self.player1.wins += 1

                q = input('Do you continue the game? (Y/n)')
                if q == 'N' or q == 'n':
                    break

        print('\nPlayer1 wins {} times.'.format(str(self.player1.wins)))
        print('Player2 wins {} times.'.format(str(self.player2.wins)))
        if self.player1.wins > self.player2.wins:
            print('Player1 wins at last.')
        elif self.player2.wins > self.player1.wins:
            print('Player2 wins at last.')
        else:
            print('Draw')

gameone = Game()
gameone.play()
