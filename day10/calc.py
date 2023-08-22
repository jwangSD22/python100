from art import calculator_image
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate(first,second,operation):
    if operation == '+':
        return float(first+second)
    
    if operation == '-':
        return float(first-second)
    
    if operation == '*':
        return float(first*second)
    
    if operation == '/':
        return float(first/second)
    


current = None

while True:

    print(calculator_image)
    first_num = None
    second_num = None

    if current == None:
        first_num = float(input('What is the first number?: '))
    else:
        first_num = current

    operation = input('Pick an operation (+, - *, /): ')

    second_num = float(input('What is the second number?: '))

    answer = calculate(first_num,second_num,operation)

    print (f'\n{first_num} {operation} {second_num} --> The answer is: {answer}\n')

    selection = input('Would you like to proceed with another calculation? (y)es, (n)o  ')

    if selection == 'n':
        current = None
    else:
        current = answer
    
    clear_console()

