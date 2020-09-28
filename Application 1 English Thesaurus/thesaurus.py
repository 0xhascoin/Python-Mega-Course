import json
from difflib import get_close_matches

data = json.load(open('English Thesaurus/data.json'))

def translate(word):
    
    # Turn the inputted word into lowercase
    word = word.lower()

    # If the inputted word is in the dictionary then return the definition
    if word in data:
        return data[word][0]
    
    # If the word is not in the dictionary BUT has close matches, ask if they meant the MOST similar
    elif len(get_close_matches(word, data.keys())) > 0:
        did_you_mean = input(f'Did you mean {get_close_matches(word, data.keys())[0]}? (Y/N) ')

        # If they meant the most similar and typed 'y', then return the meaning of that word
        if did_you_mean.lower() == 'y':
            return f'{get_close_matches(word, data.keys())[0].title()} : {data[get_close_matches(word, data.keys())[0]][0]}'

        # If they didn't mean the most similar word then tell them the word is not in the dictionary
        else:
            return 'Sorry, word not in dictionary'
    
    # If the word has no similar matches and is not in the dictionary then tell them.
    else:
        return 'Word not in dictionary'

input_word = input('Enter a word: ')

print(translate(input_word))
