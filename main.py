import os
from random import randint

words = []
mistakes = 0
word = '' #random word from words list
tip = ''  #tip for selected word
puzzle = []
guessed_letters = []
hangman_pics = []

def get_hangman_pics():
    global hangman_pics
    with open('pics.txt','r') as pics:
        for line in pics:
            hangman_pics.append(line)
    hangman_pics = ''.join(hangman_pics).split(',')

def create_word_list():
    global words
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

def print_game_status():
    os.system('clear')
    print(hangman_pics[mistakes])
    print('Tip : ' + tip)
    print(''.join(puzzle))


def guess_letter(letter):
    if letter in word.lower() and letter not in guessed_letters:
        guessed_letters.append(letter)
        for i in range(len(word)):
            if letter == word.lower()[i]:
                puzzle[i] = letter[0]
    elif letter in guessed_letters:
        print("You've already guessed that letter!")
    else:
        print("That letter does not exit in puzzle!")
        guessed_letters.append(letter)
        global mistakes
        mistakes += 1


def start_game():
    get_hangman_pics()
    create_word_list()
    get_random_word()
    create_puzzle(word)
    while '_' in puzzle:
        guess_letter(input("Guess a letter\n"))
        print_game_status()
        

start_game()
