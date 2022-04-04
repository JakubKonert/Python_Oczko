from Deck import Deck
from Player import Player

class Oczko:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)
        self.Player_status = True
        self.Dealer_status = True

    def play(self):
        while self.Player_status:
            self.player.drawCard()
            self.player.show()
            message = input("More? [Y/N]")
            if message.lower() == 'n':
                self.Player_status = False

        while self.Dealer_status and self.player.LOSE == False:
            if self.dealer.score <=17:
                self.dealer.drawCard()
                self.dealer.show()
            else:
                self.Dealer_status = False


        if (self.player.score > self.dealer.score and self.player.LOSE == False) or (self.player.LOSE == False and self.dealer.LOSE == True):
            print(f"Player WIN! Score: {str(self.player.score)}")
            print(f"Dealer Score: {str(self.dealer.score)}")
        elif self.player.score <= self.dealer.score and self.dealer.LOSE == False:
            print(f"Dealer WIN! Score: {str(self.dealer.score)}")
            print(f"Player Score: {str(self.player.score)}")
        elif self.player.LOSE == True and self.dealer.LOSE == True:
            print("Both players are lose!")


Game = Oczko()
Game.play()