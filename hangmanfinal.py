# Author: Gabriel Lojo
# Email: glojo@umass.edu
# Spire ID: 34808847

import random

def print_gallows(attempts):
    if attempts == 6:
        print("      __________\n      |        |\n      |        |\n      |\n      |\n      |\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 5:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |\n      |\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 4:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |        |\n      |\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 3:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |       /|\n      |\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 2:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |       /|\\\n      |\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 1:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |       /|\\\n      |       /\n      |\n      |\n      |\n      |\n-------------")
    elif attempts == 0:
        print("      __________\n      |        |\n      |        |\n      |        O\n      |       /|\\\n      |       / \\\n      |\n      |\n      |\n      |\n-------------")



def make_solution(a):
    if a == "NORMAL":
        words = ("VOLCANO", "PYRAMID", "ASTRONAUT", "AVOCADO", "TELESCOPE", "PINEAPPLE", "AIRPLANE", "CHOCOLATE", "NEBULA", "CUCUMBER", "GALAXY", "FIRETRUCK", "SANDWICH", "MOUNTAIN", "UNIVERSE", "TREASURE", "SUNFLOWER", "TORNADO", "UMBRELLA", "COMPUTER")
    elif a == "ANIMALS":
        words = ("ELEPHANT", "GIRAFFE", "KANGAROO", "DOLPHIN", "TIGER", "RHINOCEROS", "HIPPOPOTAMUS", "PENGUIN", "CROCODILE", "GIRAFFE", "WHALE", "CHAMELEON", "SQUIRREL", "GORILLA", "ZEBRA", "LION", "PEACOCK", "BISON", "OSTRICH", "TURTLE")
    elif a == "COUNTRIES":
        words = ("BRAZIL", "CANADA", "AUSTRALIA", "INDIA", "GERMANY", "FRANCE", "JAPAN", "MEXICO", "ITALY", "SPAIN", "ARGENTINA", "RUSSIA", "SOUTH AFRICA", "SWEDEN", "NORWAY", "EGYPT", "THAILAND", "INDONESIA", "GREECE", "TURKEY")
    elif a == "MOVIES":
        words = ("INCEPTION", "TITANIC", "AVATAR", "GLADIATOR", "INTERSTELLAR", "JURASSIC PARK", "FORREST GUMP", "THE GODFATHER", "PULP FICTION", "THE MATRIX", "THE DARK KNIGHT", "FIGHT CLUB", "STAR WARS", "CASABLANCA", "THE SHINING", "TOY STORY", "BACK TO THE FUTURE", "THE LION KING", "FROZEN", "BLACK PANTHER")
    elif a == "SHOWS":
        words = ("BREAKING BAD", "FRIENDS", "GAME OF THRONES", "STRANGER THINGS", "THE OFFICE", "SHERLOCK", "THE SIMPSONS", "FAMILY GUY", "THE MANDALORIAN", "WESTWORLD", "HOW I MET YOUR MOTHER", "THE WALKING DEAD", "BETTER CALL SAUL", "BIG BANG THEORY", "RICK AND MORTY", "HOUSE OF CARDS", "LOST", "MODERN FAMILY", "SUPERNATURAL", "BLACK MIRROR")
    elif a == "BOOKS":
        words = ("MOBY DICK", "PRIDE AND PREJUDICE", "TO KILL A MOCKINGBIRD", "THE GREAT GATSBY", "THE HOBBIT", "WAR AND PEACE", "BRAVE NEW WORLD", "THE CATCHER IN THE RYE", "LORD OF THE FLIES", "CRIME AND PUNISHMENT", "THE ALCHEMIST", "JANE EYRE", "WUTHERING HEIGHTS", "THE HUNGER GAMES", "HARRY POTTER", "LITTLE WOMEN")
    else:
        words = ("HANGMAN",)
    return random.choice(words)

def print_length(soln, guessed_letters):
    for char in soln:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def get_guess():
    guess = input("Guess a letter or word: ").upper()
    return guess

def check_guess(soln, attempts, guessed_letters):
    while attempts > 0:
        print_gallows(attempts)
        print_length(soln, guessed_letters)
        guess = get_guess()
        if len(guess) == 1:
            if not guess.isalpha():
                print("That's not a letter, you get a redo!")
                continue
            if guess in guessed_letters:
                print("You have already guessed that letter, you get a redo!")
                continue
            guessed_letters.append(guess)
            if guess in soln:
                print(f'You guessed correctly, {guess} is in the word!')
                if all(char in guessed_letters for char in soln):
                    print(f"YOU WIN! The word was {soln}.")
                    return
            else:
                attempts -= 1
                print(f"Your guess was incorrect, {guess} is not in the word.")
        else:
            if guess == soln:
                print(f"YOU WIN, Thanks for playing! The word was {soln}!")
                return
            else:
                attempts -= 1
                print(f"That's not the correct word! You have {attempts} attempts left")
    print_gallows(attempts)
    print_length(soln, guessed_letters)
    print(f"Nice try but you lost, the word was {soln}!")

def players():
    numplayers = (input("How many people are playing? (1 or 2) "))
    if numplayers.isdigit() and int(numplayers) in [1, 2]:
        attempts = 6
        guessed_letters = []
        if int(numplayers) == 1:
            a = input("Awesome, Let's Play! What Category Would You Like Your Word to Be From? (NORMAL, ANIMALS, COUNTRIES, MOVIES, SHOWS, or BOOKS) ").upper()
            soln = make_solution(a)
        elif int(numplayers) == 2:
            soln = input("Enter a word for the other player to guess: ").upper()
        check_guess(soln, attempts, guessed_letters)
    else:
        print("Please enter '1' or '2'!")
        players()

def setup():
    intro = input("Hi Welcome to Hangman! Would You like to Play? (YES or NO) ")
    if intro.upper() == "YES":
        players()
    elif intro == "NO":
        print("Lame, you stink!")
        exit()
    else:
        print("'YES' or 'NO'!")
        setup()

def play_hangman():
    setup()

play_hangman()
