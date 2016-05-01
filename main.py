import os
from random import randint


words = []
word = ''
tip = ''


def create_word_list():
    with open('words.txt', 'r') as word_list:
        for line in word_list:
            words.append(line.rstrip().split(' - '))

def get_random_word():
    rnd = randint(0,len(words) - 1)
    global tip, word
    tip = words[rnd][0]
    word = words[rnd][1]


create_word_list()
get_random_word()
print(tip + " - " + word)
