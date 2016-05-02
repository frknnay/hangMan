import os
from random import randint


words = []
word = '' #random word from words list
tip = ''  #tip for selected word
puzzle = []
guessed_letters = []


def create_word_list():
    with open('words.txt', 'r') as word_list:
        for line in word_list:
            words.append(line.rstrip().split(' - '))

def get_random_word():
    rnd = randint(0,len(words) - 1)
    global tip, word
    tip = words[rnd][0]
    word = words[rnd][1]

def create_puzzle(word):
    global puzzle
    for letter in word:
        if letter == ' ':
            puzzle.append(' ')
        else:
            puzzle.append('_')


def guess_letter(letter):
    if letter in word.lower() and letter not in guessed_letters:
        guessed_letters.append(letter)
        for i in range(len(word)):
            if letter == word.lower()[i]:
                puzzle[i] = letter[0]
    elif letter in guessed_letters:
        print("You've already guessed that letter")
    else:
        print("That letter does not exit in puzzle")

def start_game():
    create_word_list()
    get_random_word()
    print(tip + " - " + word)
    create_puzzle(word)
    print(''.join(puzzle))
    while '_' in puzzle:
        guess_letter(input("Guess a letter\n"))
        #os.system('clear')
        print(''.join(puzzle))

start_game()
