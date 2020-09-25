import json

data = json.load(open('English Thesaurus/data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return 'Word not in dictionary'

input_word = input('Enter a word: ')

print(translate(input_word))