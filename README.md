# 🌸 sudokuGame.py
A small, light (0.5 MB) implementation of the classic, logic-based game of [Sudoku](https://en.wikipedia.org/wiki/Sudoku), made primarily as a learning project inspired by an algorithmic problem. 
The game is complete with a coordinates system, user interface and victory validation and can be played on several difficulties, each with a couple of levels available.

<img src="/screenshots/activeGame.jpg" width="500px">

## About
After finishing a small algorithmic problem concerning the validation of a filled out sudoku ( [sudokuValidation.py](https://github.com/patrikmitterpach/algorithmicProblems/blob/main/Python/sudokuValidation.py) ), 
the idea seemed right to expand the function to a fully-fledged program, including a user interface, 
several difficulties and levels, an intuitive system for coordinates, extensive input handling and board validation.
So after a day and half of work, I've put together a working version of the program, which seems to perform relatively well.



## Instructions
The program should be working well out of the box, just clone/download and start the `sudokuGame.py` file. Difficulty is chosen
by entering a number between 0-3 corresponding to the difficulty desired (`Random`, `Easy`, `Medium`, `Hard`). After a
successful choice, the board is displayed, along with basic information about the difficulty and user input.
Commands are entered in the form of `COLUMN ROW NUMBER`, so for putting the number 5 into the upper left corner the
command would have the form of `A 1 5` or `A15`, as whitespace can be ignored. 

An error message will be displayed if the coordinates are invalid or the space is hardcoded on the board (denoted by square brackets `[ ]`) 
and user will be prompted to input a valid command. As the game points out, sometimes the player may wish to delete a
number from the board. This can be done by denoting the `NUMBER` to be `0`.

**Note:**
- Levels are stored in plaintext in sudoku.txt and additional partially-prefilled grids can be added easily.

### Difficulty Screen
<img src="/screenshots/difficultyScreen.jpg" width="500px">

### Validation of a correctly filled board
<img src="/screenshots/wonGame.jpg" width="500px">

## Open Source
All issues and pull requests will be greatly appreciated.
 
