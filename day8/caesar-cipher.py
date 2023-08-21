alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet)
temp_list = alphabet_list.copy()
hash = {}

direction_status = True
direction = ''
final_string = ''

while True:
    if direction_status == True:
        direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    else:
        direction=input("Please type in a valid selection\nType 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == 'encode' or direction == 'decode':
        break
    else:
        direction_status = False

text = input('Type your message:\n')
text = text.lower()

shift = int(input('Type the shift number:\n'))%26


for iteration in range(0,shift):
    temp_letter = temp_list.pop(0)
    temp_list.append(temp_letter)

#Create decode or encode table

if(direction=='encode'):
    for index in range (0,26):
        hash[alphabet_list[index]]=temp_list[index]
    for letter in text:
        if letter == ' ':
            final_string+=' '
        else:
            final_string += hash[letter]
    print(f'-----Your encoded message is: {final_string}-----')

elif(direction=='decode'):
    for index in range (0,25):
        hash[temp_list[index]] = alphabet_list[index]
    for letter in text:
        if letter == ' ':
            final_string+=' '
        else:
            final_string += hash[letter]
    print(f'-----Your decoded message is: {final_string}-----')


#
