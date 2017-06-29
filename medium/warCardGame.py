# warCardGame.py - implementation of card game War
# Made by @Atropos148

from random import shuffle

print('WAR')


class Card:
    'Common class for all playing cards'
    cardCount = 0

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        Card.cardCount += 1

    def displayCount(self):
        print('Cards total %d', Card.cardCount)

    def displayCard(self):
        print('V: {}, S: {}'.format(self.value, self.suit))


class Player:
    playerCount = 0

    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.handDeck = []
        Player.playerCount += 1

    def getCard(self, card):
        self.handDeck.append(card)

    def showHand(self):
        print('Player Number {}'.format(self.number))
        for card in self.handDeck:
            card.displayCard()


def createDeck():
    cardsList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    cardsSuits = ['clubs', 'spades', 'diamonds', 'hearts']
    deckNew = []

    for x in cardsSuits:
        for y in cardsList:
            card = Card(y, x)
            # card.displayCard()
            deckNew.append(card)
    return deckNew


deck = createDeck()
shuffle(deck)
player1 = Player(1, 'One')
player2 = Player(2, 'Two')

x = 0
for card in deck:
    if x == 0:
        player1.getCard(card)
        x = 1
    else:
        player2.getCard(card)
        x = 0

player1.showHand()
print('\n')
player2.showHand()
