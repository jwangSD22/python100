from art import logo
import os
import random


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



difficulty_hard = None
attempts = None
win_status = None

def initialize():
    clear_console()
    print(logo)
    print ('Welcome to the number guessing game!')
    print ('I am thinking of a number between 1 and 100.')
    selection = input('Choose a difficulty. (e)asy or (h)ard: ')
    global difficulty_hard

    if selection == 'h':
        attempts = 5
    else:
        attempts = 10    

    guessing_game(attempts)


def end_game(win_status):
    clear_console()
    if win_status:
        print(logo)
        print('\nYOU WIN!!!\n')
        selection = input('Play again? Input (y)es or (n)o: ')
        if (selection == 'y'):
            initialize()
    else:
        print(logo)
        print('\nYOU LOSE!!!\n')
        selection = input('Play again? Input (y)es or (n)o: ')
        if (selection == 'y'):
            initialize()
     



def guessing_game(attempts):
    random_number = random.randint(1,101)
    too_high = None
    too_high_text = 'Too high. Try again!'
    too_low_text = 'Too Low. Try again!'
    win_status = None

    while True:
        clear_console()
        print(logo)
        print(f'You have {attempts} attempts remaining!')
        if too_high==True:
            print(f'{too_high_text}')
        elif too_high==False:
            print(f'{too_low_text}')
        else:
            print('')
        selection = int(input('Make a guess: '))
        if selection > random_number:
            attempts -=1
            too_high = True
        else:
            too_high = False
            attempts -=1
        
        if attempts == 0:
            win_status = False
            break

        if selection == random_number:
            win_status = True
            break

    end_game(win_status)

initialize()
