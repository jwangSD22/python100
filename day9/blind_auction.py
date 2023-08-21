import gavel
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

hash = {}

while True:
    print (gavel.art)
    print (f'Welcome to the secret auction program.')

    name = input('What is your name?\n')
    bid = int(input('What is your bid?\n$'))

    if name not in hash:
        hash[name] = bid

    new_user_input = input('Is there another bidder? (y)es or (n)o\n')
    if new_user_input == 'y':
        clear_console()
    else:
        break

highest_amt = 0
highest_bidder = ''

for bidder in hash:
    if hash[bidder]>highest_amt:
        highest_amt = hash[bidder]
        highest_bidder = bidder

print(f'{highest_bidder} wins the auction with a bid of ${highest_amt}')
