import random
#todo - switching letters for blanks and printing
#todo - expand the the of words to dictionary list

d_list = ["mouse", "crocodile","zebra"]
hangman = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
YOU LOSE H A H A H A H A""","""
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
word_blanks = []
#random word from the list choice
chosen_word = random.choice(d_list)
print(chosen_word)

letters = list(chosen_word)#letters as a list

#blanks printout
blanks = len(chosen_word)
br=0
while br!=blanks:
    one_blank = '_'
    word_blanks.append(one_blank)
    br+=1
normal_word_blanks =  " ".join(word_blanks)
print("Word to guess: ",normal_word_blanks)#blanks but in normal mode lol
print(list(normal_word_blanks))#TODO -  use this transformation to acess blanks and change them for letters

#todo - not finished gameplay
life = 6
letters_guessed = ""
while(life!=0):
    guess = input("Guess a letter: ")
    lower_case_guess = guess.lower()
    letters_guessed+=lower_case_guess

    print(lower_case_guess)
    if (lower_case_guess in chosen_word):

        print(f"******************{life}/6 lifes left**************")
        print("Guessed letters: ",",".join(letters_guessed))
        print(hangman[life])

    else:
        print('wrong')
        life-=1
        print(f"******************{life}/6 lifes left**************")
        print("Guessed letters: ",",".join(letters_guessed))
        print(hangman[life])




