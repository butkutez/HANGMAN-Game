import random
import json
from stages import render_stage

class Hangman:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.user_answer = ["_"] * len(word)
        self.dashes = "-" * 30
        self.misses = 0
        self.MAX_MISSES = 6
        self.entered_letters = set()
    
    def print_header(self):
        print(self.dashes)
        print("\tH A N G M A N")
        print(self.dashes)

    def print_goodbye(self):
        print(self.dashes)
        print("\tG O O D B Y E")
        print(self.dashes)

    def play(self):
        self.print_header()

        while True:
            render_stage(self.misses)
            self.display_status()

            guess = input("\nGuess a letter: ").strip().upper()                     
            self.process_guess(guess)
            print(f"\n{self.dashes}")

            if self.is_won() or self.is_lost():
                render_stage(self.misses)
                self.display_result()
                break
    
    def process_guess(self, guess):
        if not guess.isalpha() or len(guess) != 1:
            print("\nInvalid input! You can only enter alphabets (A-Z).")
            return

        if guess in self.entered_letters:
            print("\nYou've already guessed that letter!")
            return
        self.entered_letters.add(guess)
  
        if guess in self.word:
            for i, c in enumerate(self.word):
                if c == guess:
                    self.user_answer[i] = guess
            print("\nCorrect!")
        else:
            print("\nIncorrect!")
            
            self.misses += 1
        return True
 
    def is_won(self):
        return "_" not in self.user_answer

    def is_lost(self):
        return self.misses >= self.MAX_MISSES

    def display_result(self):
        if self.is_won():
            print("\nWord:", " ".join(self.user_answer))
            print("\nYou won!")
            print(f"\n{self.dashes}")

        if self.is_lost():
            print(f"\nMisses: {self.misses} / {self.MAX_MISSES}")
            print("\nYou lose!")
            print(f"\nThe word was: {self.word}")
            print(f"\n{self.dashes}")

    def display_status(self):
        print("\nCurrent:", " ".join(self.user_answer))
        print(f"\nHint: {self.hint}")
        print("\nAlready Guessed:", ", ".join(sorted(self.entered_letters)))
        print(f"\nMisses: {self.misses} / {self.MAX_MISSES}")
        
while True:
    with open("words.json", "r") as f:
        words_list = json.load(f)
    
    selected = random.choice(words_list)
    word = selected["word"].upper()
    hint = selected["hint"]
    
    game = Hangman(word, hint)
    game.play()

    # Reset prompt
    choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
    if choice != "Y":
        game.print_goodbye()
        break



        