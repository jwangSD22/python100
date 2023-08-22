suits_hash = {
    'Spades':'♠',
    'Diamonds':'♦',
    'Hearts': '♥',
    'Clubs':'♣',
    'hidden':'hidden'
}

values_hash = {
   'Ace':'A',
   '2':'2',
   '3':'3',
   '4':'4',
   '5':'5',
   '6':'6',
   '7':'7',
   '8':'8',
   '9':'9',
   '10':'10',
   'Jack':'J',
   'Queen':'Q',
   'King':'K',
   'hidden':'hidden'
}





def card_image(value,suit):
    if(value=='10'):
        return f"""
┌─────────┐
|{suits_hash[suit]}{values_hash[value]}      |
|         |
|         |
|    {suits_hash[suit]}    |
|         |
|         |
|      {suits_hash[suit]}{values_hash[value]}|
└─────────┘
"""
    if(value=='hidden'):
        return f"""
┌─────────┐
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
└─────────┘
"""
    else:
        return f"""
┌─────────┐
|{suits_hash[suit]}{values_hash[value]}       |
|         |
|         |
|    {suits_hash[suit]}    |
|         |
|         |
|       {suits_hash[suit]}{values_hash[value]}|
└─────────┘
"""

def multiple(card1,card2,cpu=False):
    final = ''
    img1 = None
    img2 = None
    if cpu==True:
        img1 = card1.split('\n')
        img2 = card_image('hidden','hidden').split('\n')


        for [one,two] in zip(img1, img2):
            final+=one + '  ' + two + '\n'
        return final 

    if card1 == None:
        return card_image(card2[0],card2[1])
    else:
        img1 = card1.split('\n')
        img2 = card_image(card2[0],card2[1]).split('\n')


    for [one,two] in zip(img1, img2):
        final+=one + '  ' + two + '\n'
    return final


def gen_hidden_image(card1,card2):
    final = ''
    img1 = None
    img2 = None

    img1 = card1.split('\n')
    img2 = card_image('hidden','hidden').split('\n')


    for [one,two] in zip(img1, img2):
        final+=one + '  ' + two + '\n'
    return final 
