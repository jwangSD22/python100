import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_dict = {v.letter:v.code for (i,v) in df.iterrows()}

def convertNATO(name):
    return [lookupLetter(n) for n in name]


def lookupLetter(n):
    upper = n.upper()
    return nato_dict[upper]



def app():

    while True:
        try:
            response = input('Enter a word to conver to NATO phonetic alphabet: ')
            print(convertNATO(response))
            break

        except KeyError:
            print('Please enter only valid characters of alphabet.')


app()