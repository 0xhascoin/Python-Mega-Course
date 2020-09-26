import json
from difflib import get_close_matches

data = json.load(open('English Thesaurus/data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        did_you_mean = input(f'Did you mean {get_close_matches(word, data.keys())[0]}? (Y/N)')

        if did_you_mean.lower() == 'y':
            # 
        else:
            # 
    else:
        return 'Word not in dictionary'

input_word = input('Enter a word: ')

print(translate(input_word))
