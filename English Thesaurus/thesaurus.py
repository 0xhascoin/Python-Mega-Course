import json

data = json.load(open('English Thesaurus/data.json'))

def translate(word):
    return data[word]

input_word = input('Enter a word: ')

print(translate(input_word))