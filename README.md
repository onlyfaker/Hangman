# Python Hangman Game 🎮

A classic command-line implementation of the Hangman game written in Python. Players try to guess a word by suggesting letters, with a limited number of wrong guesses allowed before the game ends.

## 📝 Description

This Hangman game is a text-based version of the classic paper and pencil guessing game. The game randomly selects a word from a predefined list, and players must guess it letter by letter. For each wrong guess, a part of the hangman is drawn. The game continues until either:
- The player successfully guesses the word
- The hangman drawing is completed (after 6 wrong guesses)

## 🚀 Features

- ASCII art title display
- Visual hangman progression using ASCII art
- Word list with 100 words across various categories
- Letter guess tracking
- Input validation
- Lives counter
- Already guessed letters display
- Case-insensitive letter matching

## 🛠️ Project Structure

```
hangman/
│
├── main.py           # Main game logic
├── hangman_art.py    # ASCII art for game title
└── hangman_words.py  # List of words for the game
```

## 📋 Prerequisites

- Python 3.x

## 🎮 How to Play

1. Clone the repository:
```bash
git clone [your-repository-url]
```

2. Navigate to the game directory:
```bash
cd hangman
```

3. Run the game:
```bash
python main.py
```

4. Game Rules:
   - The game will display blanks representing each letter in the word
   - Guess one letter at a time
   - For each incorrect guess, a part of the hangman is drawn
   - You have 6 lives (wrong guesses) before the game ends
   - Repeated guesses don't count against your lives
   - Win by correctly guessing all letters in the word

## 🎯 Game Features Explained

### Input Validation
- Only single letter inputs are accepted
- Repeated guesses are caught and handled
- Case-insensitive letter matching

### Display Features
- ASCII art title
- Visual hangman progression
- Current word state with revealed letters
- List of previously guessed letters
- Remaining lives counter

### Word Categories
The game includes words from various categories:
- Technology and Computing
- Animals and Nature
- Food and Drinks
- Sports and Activities
- Science and Education
- And more!

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can:
- Add more words to the word list
- Improve the ASCII art
- Add new features
- Fix bugs
- Improve code documentation

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🎨 Credits

Created by AG

---
Feel free to star ⭐ this repository if you find it helpful!
