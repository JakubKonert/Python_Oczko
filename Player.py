from Deck import Deck

class Player:
    def __init__(self,isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.score = 0
        self.deck = deck
        self.LOSE = False


    def checkScore(self):

            self.score += self.cards[-1].cost

    def drawCard(self):
        self.cards = self.deck.draw(self.cards)
        self.checkScore()

    def show(self):
        if self.isDealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for card in self.cards:
            card.show()

        print("Score: " + str(self.score))

        if self.score > 21:
            self.LOSE = True        