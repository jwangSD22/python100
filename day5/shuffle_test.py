#Fisher-Yates shuffle algorithm??

import random

my_string = 'abcdefghijklmnopqrstuvwxyz'

container = list(my_string)


for num in range(0,len(container)):
    random_num = random.randint(0,len(container)-1)
    [container[num],container[random_num]] = [container[random_num],container[num]]

final=''.join(container)

print(final)
