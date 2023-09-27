import random
from itertools import chain

def pwgenfunction():
    #lists of all the possible choices from each category
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list ('!@#$%^&*()+')

    #main user interface
    nr_letters = 8
    nr_symbols = 4
    nr_numbers = 4

    #accessory function to generate random values from a list with a parameter indicating number of characters
    def get_random_from_list(list,number):
        container = []
        while number>0:
            container.append(random.choice(list))
            number-=1
        return container


    #contain all of the values randomly generated based on user selections and flatt en into a single list
    my_letters = get_random_from_list(letters,nr_letters)
    my_symbols  = get_random_from_list(symbols,nr_symbols)
    my_numbers = get_random_from_list(numbers,nr_numbers)
    container = [my_letters,my_numbers,my_symbols]
    flattened = list(chain.from_iterable(container))

    # You can simply use random.shuffle to shuffle your lists.
    random.shuffle(flattened)
    # You can also join str_elements of an array by using
    joined_string = ''.join(flattened)


    #randomly insert all the values into the final password
    final = ''
    while len(flattened):
        selected = random.randint(0,len(flattened)-1)
        popped = flattened.pop(selected)
        final+=popped



    return final

