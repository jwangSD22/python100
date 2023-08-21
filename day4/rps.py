import random

while True:
    
    your_choice = int(input('What do you choose? Rock[0], Paper[1], Scissors[2]\n'))
    if your_choice > 2:
        print('Please select a valid number...\n\n')
    else: break

cpu_choice = random.randint(0,2)

def print_choice(arg):
    if arg == 0:
        return 'Rock'
    if arg == 1:
        return 'Paper'
    if arg == 2:
        return 'Scissors'
    

if your_choice==cpu_choice:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n GAME DRAW!")
if your_choice==0 and cpu_choice==1:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n CPU WINS!")
elif your_choice==0 and cpu_choice==2:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n YOU WIN!")
if your_choice==1 and cpu_choice==0:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n YOU WIN!")
elif your_choice==1 and cpu_choice==2:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n CPU WINS!")
if your_choice==2 and cpu_choice==1:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n YOU WIN!")
elif your_choice==2 and cpu_choice==0:
    print(f"You selected {print_choice(your_choice)}. CPU selected {print_choice(cpu_choice)}\n CPU WINS!")


