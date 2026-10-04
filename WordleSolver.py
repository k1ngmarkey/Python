from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_words(filename: str) -> list:
    with open(BASE_DIR / filename) as file:
        return [line.strip() for line in file if line.strip()]

answers = load_words("valid_wordle_answers.txt")
guesses = load_words("valid_wordle_guesses.txt")

def play_wordle(words : list) -> None:
    """Eliminate incorrect words"""
    while len(words) > 1:
        letters_in_word = []
        for position in range(5):
            letter = input("What letter did you put in position" + str(position + 1) + "?: ").lower()
            color = input("What color is it (g,y,b)?: ").lower()
            if color != 'g' and color != 'y' and color != 'b':
                print("invalid input")
                return
            words_to_remove = []
            for word in words:
                if color == 'g':
                    if word[position] != letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                elif color == 'y':
                    if letter not in word:
                        words_to_remove.append(word) 
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                    elif word[position] == letter:
                        words_to_remove.append(word)
                elif color == 'b':
                    if letter in word:
                        if letter not in letters_in_word:
                            words_to_remove.append(word)
                        elif words[position] == letter:
                            words_to_remove.append(word)
            for w in words_to_remove:
                words.remove(w)
        print(words)
        guess = input("Did you guess correctly y/n")
        if guess == 'y':
            print("Nice job cheating!")
            return
play_wordle(answers)

