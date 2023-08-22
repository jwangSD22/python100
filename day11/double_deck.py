double_deck_template = []

card_values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

suits = ['Spades','Hearts','Clubs','Diamonds']

for n in range(0,2):
    for suit in suits:
        for card in card_values:
            double_deck_template.append([card,suit])


