import random
#todo - switching letters for blanks and printing
#todo -  life score print
#todo - expand the the of words to dictionary list
#todo -
d_list = ["mouse", "crocodile","zebra"]
hangman = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""","""
  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========""","""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""","""
  +---+
  |   |
  O   |
  |\  |
      |
      |
=========""","""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""","""
  +---+
  |   |
  0   |
      |
      |
      |
=========""","""
  +---+
  |   |
      |
      |
      |
      |
========="""]
word_blanks_letters = []
#random word from the list choice
chosen_word = random.choice(d_list)
print(chosen_word)

#blanks printout
blanks = len(chosen_word)
br=0
print("word to guess:")
while br!=blanks:
    one_blank = '_'
    print(one_blank,end=" ")
    word_blanks_letters.append(one_blank)
    br+=1
print()
print(" ".join(word_blanks_letters))#blanks but in normal mode lol

#todo - not finished gameplay
life = 6
while(life!=0):
    guess = input("guess the letter: ")
    guess.lower()

    if (guess in chosen_word):
        print("right")
        print(hangman[life])
    else:
        print('wrong')
        life-=1
        print(hangman[life])



