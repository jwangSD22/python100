import os
import random
from art import logo
from double_deck import double_deck_template as deck
from card_image_gen import card_image as gencard
from card_image_gen import multiple as genimgs

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_value(value_str,softness=False):
    if value_str == 'A':
        return 1
    if value_str == 'J' or value_str == 'Q' or value_str == 'K':
        return 10
    else:
        return value_str
    


def check_soft(hand):
    for card in hand:
        if card[0] == 'A':
            return True
        else:
            return False
        
def drawcard(deck):
    random_index = random.randint(0,len(deck)-1)
    selected = deck.pop(random_index)
    return selected


class Hand:
    def __init__(self):
        self.hand=[]
        self.value = 0
        self.image = None
        self.soft = False
        self.resolved = False
        self.busted = False

    
    def add_card(self,new_card,cpu=False):
        self.hand.append([new_card[0],new_card[1]])
        self.image = genimgs(self.image,new_card,cpu)

class Blackjack:
    def __init__(self,bankroll):
        self.cpu = Hand()
        self.player = Hand()
        self.bankroll = bankroll
        self.deck = deck.copy()
        self.player_queue = []
        self.player_resolve_queue = []

    def initial_draw(self):
        self.player.add_card(drawcard(self.deck))
        self.cpu.add_card(drawcard(self.deck))
        self.player.add_card(drawcard(self.deck))
        self.cpu.add_card(drawcard(self.deck),True)

    def initialize_game(self):
        clear_console()
        print(logo)
        print('DEALER HAND')
        print(self.cpu.image)
        print('PLAYER HAND')
        print(self.player.image)
        
        
        #need to analyze current hand to determine options -- 
        #if it's a soft hand -- need to give option to ... double 
        #if the hand has two of the same cards, need to offer to split 
        


print(logo)
bank_roll = int(input('What is your initial bank-roll? $'))
game = Blackjack(bank_roll)
game.initial_draw()
game.initialize_game()



