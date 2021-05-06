import os
import random

def read(filepath = "./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding= "utf-8") as f:
        [words.append(word.replace("\n","")) for word in f]       
    return words


def run ():
    data = read(filepath="./archivos/data.txt")
    random_word = random.choice(data)
    random_word_list = [letter for letter in random_word]
    underscores = "_" * len(random_word)
    random_word_dict = {}
    for idx, letter in enumerate(random_word):
        if not random_word_dict.get(letter):
            random_word_dict[letter] = []
        random_word_dict(letter).append(idx)

palabras = read()
print(palabras)



