import os
import random
import time

def read(filepath = "./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding= "utf-8") as f:
        [words.append(word.replace("\n","")) for word in f]       
    return words

def normalize(s):
    replacement = (
        ("a","á"),
        ("e","é"),
        ("i","í"),
        ("o","ó"),
        ("u","ú"),
    )
    for a, b in replacement:
        s = s.replace(a, b)
    return s

def run():
    data = read(filepath="./archivos/data.txt")
    random_word = random.choice(data)
    random_word_list = [letter for letter in random_word]
    underscores = "_" * len(random_word)
    random_word_dict = {}
    for idx, letter in enumerate(random_word):
        if not random_word_dict.get(letter):
            random_word_dict[letter] = []
        random_word_dict[letter].append(idx)

    while True:
        os.system("cls")
        print("¡Adivina la palabra!")
        for element in underscores:
            print(element + " ", end="")
        print("\n")

        letter =input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes insertar letras"
        assert len(letter) == 1, "Ingresa solo una letra"

        if letter in random_word_list:
            for idx in random_word_dict[letter]:
                underscores[idx] = letter
                
        # if letter not in random_word_list:
        #     print("La palabra no contiene " + letter + ". Prueba otra letra")
        #     time.sleep(2)
        
        if "_" not in underscores:
            os.system("cls")
            print("Ganaste el juego " + "\n" + "La Palabra era " + random_word)

if __name__ == '__main__':
    run()


