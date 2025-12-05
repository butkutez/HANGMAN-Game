# The HANGMAN Game
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![Property_Price_Predictor](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3253300/header.jpg?t=1732659042)

*Image source: [STEAM](https://store.steampowered.com/app/3253300/HANGMAN/)*

## Project Description

This project is a classic game of Hangman, implemented purely in Python for the command-line terminal.

The game challenges the player to guess a secret word one letter at a time. For every incorrect guess, a part of the hangman figure is drawn. The player has a limited number of incorrect guesses before the figure is complete and the game is lost. The words and corresponding hints are loaded from an external words.json file, allowing for easy expansion of the dictionary.

The maximum number of misses allowed is 6.


## Getting started

### Installation
You need to have Python 3.x installed on your system.

**1. Clone the project**

```
cmd git clone https://github.com/butkutez/HANGMAN-Game.git
```
**2. Navigate to the project folder**
```
cd HANGMAN-GAME
```

**3. Run the main scraper**
````
python hangman.py
````

## Repo structure

```
HANGMAN-GAME
├── hangman.py
├── README.md
├── stages.py
└── words.json
```

## Usage (How to Play)

<u>Start the Game</u>: Run python hangman.py. The game will display the initial hangman stage, the dashed word, a hint, and the number of allowed misses.

<u>Guess a Letter</u>: When prompted, enter a single letter (A-Z) and press Enter. The input is not case-sensitive.

<u>Correct Guess</u>: If the letter is in the word, it will be revealed in all its positions.

<u>Incorrect Guess</u>: If the letter is not in the word, a part of the hangman will be drawn, and your remaining misses will decrease.

**Game End**:
- You win if you guess all the letters in the word before running out of misses.

- You lose if the hangman figure is completed (6 misses). The correct word will be displayed.

*Play Again*: After a game ends, you'll be asked if you want to play another round. Enter Y to continue or N to quit.

## The Core Functionality

- The game is built around the Hangman class, which manages the state of the current game.

- Word Selection: A random word and its hint are selected from the words.json file.

- The class keeps track of:

    -  self.user_answer: The list of guessed letters and remaining underscores (e.g., ['_', 'A', '_', 'S', 'E']).

    - self.entered_letters: A set of all letters already guessed to prevent duplicates.

    - self.misses: The current count of incorrect guesses.

- Visuals: The render_stage function uses ASCII art to visually represent the gallows and the hangman figure based on the self.misses count.

```
Current: _ A _ S E
Hint: A structured set of data
Already Guessed: A, D, E, S
Misses: 1 / 6
Guess a letter: 
```
## Expand the Dictionary
You can easily add new words to the game by editing the words.json file. Each entry must be a JSON object with a "word" (in uppercase) and a helpful "hint".

## Timeline

This project was completed over **3 days**, fulfilling the objective of creating a simple, engaging, and modular command-line game in Python, complete with configurable word lists and ASCII art visuals.

## Personal Situation
This project was completed as a **personal initiative** to practice core Python programming, object-oriented design (using the Hangman class), and file handling (words.json).

Connect with me on [LinkedIn](https://www.linkedin.com/in/zivile-butkute/).



[![Gaming GIF](https://media1.tenor.com/m/i1Hn_Rkco4IAAAAC/controller-grass.gif)](https://tenor.com/en-GB/view/controller-grass-gif-10039060118619595650)

*Image source: [tenor](https://tenor.com/en-GB/view/controller-grass-gif-10039060118619595650)*