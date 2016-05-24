import os
from random import randint


words = []
mistakes = 0
word = ''   #random word from words list
tip = ''    #tip for selected word
puzzle = []
guessed_letters = []
hangman_pics = []
error = ''

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
    print("Guessed letters: " + ",".join(guessed_letters))
    print(hangman_pics[mistakes])
    print('Tip : ' + tip)
    print(''.join(puzzle))

    if len(error) > 0:
        print("\n" + error)

def guess_letter(letter):
    global error

    while True:
        if isinstance(letter, str) and len(letter) == 1:
            break
        else:
            letter = input("\nYou should enter a letter!\n")

    if letter in word.lower() and letter not in guessed_letters:
        error = ''
        guessed_letters.append(letter)
        for i in range(len(word)):
            if letter == word.lower()[i]:
                puzzle[i] = letter[0]

    elif letter in guessed_letters:
        error = "You've already guessed that letter!"


    else:
        error = "That letter does not exit in puzzle!"
        guessed_letters.append(letter)
        global mistakes
        mistakes += 1

    if mistakes == 6:
        print("You've run out of guesses!")
        exit()

def start_game():
    get_hangman_pics()
    create_word_list()
    get_random_word()
    create_puzzle(word)
    while '_' in puzzle:
        print_game_status()
        guess_letter(input("Guess a letter: "))


start_game()
