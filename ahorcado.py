import os
import random

def read():
    words = []
    with open("./data.txt", "r", encoding= "utf-8") as f:
        [words for word in f]
    return words
    



