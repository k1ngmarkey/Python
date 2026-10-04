# Wordle Solver

This project is a small Python command-line helper for narrowing down possible Wordle answers based on feedback from a guess.

It reads a list of valid Wordle words, asks the user for the letter/color feedback for each position, removes impossible candidates, and prints the remaining words.

## Features

- Loads candidate words from a text file
- Asks the user for each letter in the guessed word
- Accepts feedback using Wordle colour codes:
  - `g` = green
  - `y` = yellow
  - `b` = black
- Filters the candidate list based on that feedback
- Displays the remaining possible answers
- Stops when the user confirms the answer was guessed correctly

## Requirements

- Python 3
- A file named `valid_wordle_answers.txt` in the same directory as the script
- Optional: `valid_wordle_guesses.txt` (loaded by the script, but not currently used in the main logic)

## Files

- `WordleSolver.py` — main script
- `valid_wordle_answers.txt` — list of valid Wordle solution words
- `valid_wordle_guesses.txt` — list of valid Wordle guess words

## How to Run

From the directory containing the script, run:

```bash
python WordleSolver.py
```

Then follow the prompts:

- Enter the letter in each position
- Enter the colour feedback for that letter:
  - `g` for green
  - `y` for yellow
  - `b` for black

The script will repeatedly narrow the list of possible words and print the surviving candidates.

## How It Works

The program does the following:

1. Loads all word candidates from `valid_wordle_answers.txt`
2. Repeatedly asks for letter and colour feedback
3. Removes words that are inconsistent with the feedback
4. Prints the remaining valid candidates
5. Stops when the user answers that the word was guessed correctly

## Notes

This is a manual Wordle helper, not a fully automatic solver.

The script is a simple prototype:
- it does not automatically choose the next guess
- it relies on the user to enter feedback
- it loads `valid_wordle_guesses.txt`, but the current version does not use that list in the solving process

## Example

A typical interaction looks like this:

```text
What letter did you put in position1?: s
What colour is it (g,y,b)?: b
What letter did you put in position2?: t
What color is it (g,y,b)?: y
...
```

After each input, the script removes unsuitable words and prints the remaining possibilities.

## License

This project does not include a license file, so my terms govern usage unless otherwise specified.
