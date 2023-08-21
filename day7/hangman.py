import random

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the console




word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
filtered_words = list(filter(lambda word: "'" not in word, WORDS))

# selected = filtered_words[random.randint(0,len(filtered_words))].lower()

selected = 'monkey'

length = len(selected)

guesses = 5
hash = {}
win_status = ''

while (win_status != False) or (win_status != True):
    clear_console()
    display = ''
    for letter in selected:
        if letter in hash:
            display+=letter+' '
        else:
            display+='_ '

    print(f'{display}\n')
    print(f'You have {guesses} remaining\n')

    letter = input('Pick a letter\n')
    if letter not in hash:
        hash[letter] = True
    #Check hash against selected word 
    if letter in selected:
        count = len(selected)
        for letter in selected:
            if letter in hash:
                count-=1
                if count == 0:
                    win_status = True
        if win_status == True:
            break            
                    
                    

        #check win conditions -- if every letter was found 
    else:
        guesses-=1
        if guesses == 0:
            win_status = False
            break


if win_status == True:
    clear_console()
    display=''
    for letter in selected:
        if letter in hash:
            display+=letter+' '
        else:
            display+='_ '
    print(f'{display}\n')
    print(f'You have {guesses} remaining\n')
    print('YOU WIN!!!!!!!!!!!!!!!!!!')

else:
    clear_console()
    print(f'{display}\n')
    print(f'You have {guesses} remaining\n')
    print('YOU LOSE!!!!!!!!!!!!!!!')

