import random
from hangman_art import LOGO
from hangman_words import WORD_LIST


print(LOGO,'\n')
d_list = WORD_LIST
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
word_blanks = []
#random word from the list choice
chosen_word = random.choice(d_list)
letters = list(chosen_word)#letters as a list#

#blanks print-out
blanks = len(chosen_word)
br=0
while br!=blanks:
    one_blank = '_'
    word_blanks.append(one_blank)
    br+=1

life = 6
letters_guessed = ""
counter = 0
#while we dont win, keep guessing and check if the letter is in word loop
while(life!=0):
    print("Word to guess:", " ".join(word_blanks))
    user_guess = input("Guess a letter: ")
    lower_case_guess = user_guess.lower()
    #can I check these condtitions with try and catch, and if so is it better with 'if' or 'try/catch'
    if len(user_guess) != 1:
        print("Error: Please enter exactly one letter!\n")
        continue
    if lower_case_guess in letters_guessed:
        print("Guessed letters: ",",".join(letters_guessed))
        print('You have already guessed the letter ', lower_case_guess,' :)\n')
        continue
    letters_guessed+=lower_case_guess

    if (lower_case_guess in chosen_word):
        for i in range(len(letters)):#we are getting index from here which help with letters and blanks
            if letters[i] == lower_case_guess:
                word_blanks[i] = lower_case_guess
                counter+=1
        print(" ".join(word_blanks))
        #the counter tracks condition when all the letters are guessed you win
        if counter == len(letters):
            print("\n YOU WIN!!! LESS GOOO")
            break
        print("Guessed letters: ",",".join(letters_guessed))
        print(hangman[life])
        print(f"******************{life}/6 lifes left**************")


    else:

        print('You guessed ', user_guess, ' and it is not in the word :)')
        life-=1
        print("Guessed letters: ",",".join(letters_guessed))
        print(hangman[life])
        print(f"******************{life}/6 lifes left**************")
#when done with a loop, check if we have 0 lifes, then we lose
if life==0:
    print("\n YOU LOSE H A H A H A H A\n")
    print(chosen_word)





