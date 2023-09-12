#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
        
with open('./Input/Names/invited_names.txt') as f:
    name_array = f.readlines()
    for index in range(0,len(name_array)-1):
        name_array[index]=name_array[index][0:-1]
    
        
   
print(name_array)

def replace_letter(name):
    with open('./Input/Letters/starting_letter.txt') as f:
        letter_lines = f.readlines()
        letter_lines[0] = letter_lines[0].replace('[name]',name)
    letter_lines
        
    with open(f'./ReadyToSend/{name}.txt',mode='w') as f:
        f.writelines(letter_lines)

for name in name_array:
    replace_letter(name)
