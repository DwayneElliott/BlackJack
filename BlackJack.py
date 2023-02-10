import random

class Blackjack:
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.deck = [(v, s) for v in self.values for s in self.suits] * 4
        self.dealer = []
        self.player = []
        self.player_chips = 100
        
    def start_game(self):
        while True:
            print(f"You have {self.player_chips} chips.")
            bet = int(input("How much would you like to bet? "))
            if bet > self.player_chips:
                print("You don't have enough chips. Please try again.")
                continue
            random.shuffle(self.deck)
            
            self.dealer = [self.deck.pop(), self.deck.pop()]
            self.player = [self.deck.pop(), self.deck.pop()]
            
            print("Dealer has: {} of {} and an unknown card".format(self.dealer[1][0], self.dealer[1][1]))
            print("Player has: {}".format([f"{v} of {s}" for v, s in self.player]))
            
            while sum(v for v, s in self.player) < 21:
                choice = input("Do you want to hit or stand? ").lower()
                if choice == 'hit':
                    self.player.append(self.deck.pop())
                    print("Player has: {}".format([f"{v} of {s}" for v, s in self.player]))
                else:
                    break
            
            while sum(v for v, s in self.dealer) < 17:
                self.dealer.append(self.deck.pop())
            
            dealer_total = sum(v for v, s in self.dealer)
            player_total = sum(v for v, s in self.player)
            
            if player_total > 21:
                print("Player busts! Dealer wins.")
                self.player_chips -= bet
            elif dealer_total > 21:
                print("Dealer busts! Player wins.")
                self.player_chips += bet
            elif dealer_total < player_total:
                print("Player wins!")
                self.player_chips += bet
            elif dealer_total > player_total:
                print("Dealer wins!")
                self.player_chips -= bet
            else:
                print("It's a tie!")
            
            if self.player_chips == 0:
                print("You're out of chips! Game over.")
                break
            
            play_again = input("Do you want to play again? (yes/no) ").lower()
            if play_again == 'no':
                break

game = Blackjack()
game.start_game()
