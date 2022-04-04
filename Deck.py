import random
from Card import Card

class Deck:

    def __init__(self):
        self.numbers = {
            'A':11, 
            'K':4,
            'D':3,
            'J':2,
            '10':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,            
            '4':4,
            '3':3,
            '2':2           
            }
        self.shapes = ['♥','♦','♣','♠']
        self.cards = []

    def generate(self):
        for key, value in self.numbers.items():
            for j in range(4):
                self.cards.append(Card(key,self.shapes[j],value))


    def draw(self, cards):
        Rcard = random.choice(self.cards)
        self.cards.remove(Rcard)
        cards.append(Rcard)
        return cards