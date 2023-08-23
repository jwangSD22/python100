import art
import random
from game_data import data
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize(score = 0):
    win_status = None
    while True:
        clear_console()
        person_a = data[random.randint(0,len(data)-1)]
        person_b = data[random.randint(0,len(data)-1)]

        person_a_name = person_a['name']
        person_a_follower_count = person_a['follower_count']
        person_a_description = person_a['description']
        person_a_country = person_a['country']
        person_b_name = person_b['name']
        person_b_follower_count = person_b['follower_count']
        person_b_description = person_b['description']
        person_b_country = person_b['country']


        print(art.logo)
        print(f'\nCompare A: {person_a["name"]}, a {person_a_description}, from {person_a_country} \n')
        print(art.vs)
        print(f'\nCompare B: {person_b_name}, a {person_b_description}, from {person_b_country} \n')

        selection = input('Who has more followers? Type "A" or "B": ')

        if selection == 'a' and person_a_follower_count>person_b_follower_count:
            score+=1
        elif selection =='b' and person_a_follower_count<person_b_follower_count:
            score+=1
        else:
            win_status = False
            end_game(win_status,score)
            break

def end_game(win_status,score):
    if win_status == True:
        clear_console()
        print(art.logo)
        print('YOU WIN!!!!')
        selection = input('Play again? Input (y)es or (n)o: ')
        if(selection == 'y'):
            initialize()
    elif win_status == False:
        clear_console()
        print(art.logo)
        print(f'You lose. Final score: {score}\n\n')
        selection = input('Play again? Input (y)es or (n)o: ')
        if(selection == 'y'):
            initialize()

initialize()
