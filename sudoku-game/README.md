# Sudoku Game

A complete Sudoku game implementation in Python with puzzle generation, validation, solving, and a command-line interface.

## Features

- **Puzzle Generation**: Creates Sudoku puzzles with three difficulty levels (easy, medium, hard)
- **Game Logic**: Full validation of moves according to Sudoku rules
- **Solver**: Automatic puzzle solving using backtracking algorithm
- **CLI Interface**: Interactive command-line game with intuitive commands
- **Hints**: Get hints for the next move
- **Solution Display**: View the complete solution at any time

## Project Structure

```
sudoku-game/
├── sudoku.py          # Core Sudoku game logic
├── game.py           # Command-line interface
├── tests/
│   └── test_sudoku.py # Unit tests
└── README.md         # This file
```

## How to Play

### Starting the Game

Run the game using Python:

```bash
python3 sudoku-game/game.py
```

### Game Commands

- `new [easy|medium|hard]` - Start a new game with specified difficulty
- `solve` - Show the complete solution
- `hint` - Get a hint for the next move
- `help` - Display help information
- `quit` - Exit the game

### Making Moves

To place a number on the board, use the format: `<position> <number>`

**Position formats:**
- Use letters A-I for columns
- Use numbers 1-9 for rows
- Examples: `A1`, `B2`, `C3`, etc.
- Alternative format: `1A`, `2B`, `3C`, etc.

**Examples:**
- `A1 5` - Place number 5 at position A1
- `B2 0` - Clear position B2 (remove number)
- `C3 7` - Place number 7 at position C3

### Game Rules

Standard Sudoku rules apply:
1. Each row must contain the numbers 1-9 without repetition
2. Each column must contain the numbers 1-9 without repetition  
3. Each 3×3 box must contain the numbers 1-9 without repetition

## API Reference

### SudokuGame Class

#### Methods

- `__init__()` - Initialize a new game instance
- `generate_puzzle(difficulty: str = "medium")` - Generate a new puzzle
- `make_move(row: int, col: int, num: int) -> bool` - Make a move on the board
- `is_valid_move(row: int, col: int, num: int) -> bool` - Check if a move is valid
- `solve() -> bool` - Solve the current puzzle
- `is_complete() -> bool` - Check if puzzle is solved
- `get_hint() -> Optional[Tuple[int, int, int]]` - Get a hint
- `display_board() -> str` - Get formatted board string

#### Difficulty Levels

- **Easy**: ~40 cells removed from solution
- **Medium**: ~50 cells removed from solution  
- **Hard**: ~60 cells removed from solution

## Running Tests

To run the unit tests:

```bash
cd sudoku-game
python3 -m unittest tests/test_sudoku.py -v
```

The tests cover:
- Game initialization and setup
- Move validation and execution
- Puzzle generation and solving
- Completion detection
- Hint system
- Display formatting
- Full game workflow integration

## Example Game Session

```
🧩 Welcome to Sudoku! 🧩
Type 'help' for commands or 'new' to start a game

Sudoku> new medium
Generating new medium Sudoku puzzle...
New game started!

  ┌───────┬───────┬───────┐
1 │ 5 3   │   7   │       │
  ├───────┼───────┼───────┤
2 │ 6     │ 1 9 5 │       │
3 │   9 8 │       │   6   │
  ├───────┼───────┼───────┤
4 │ 8     │   6   │     3 │
5 │ 4     │ 8   3 │     1 │
6 │ 7     │   2   │     6 │
  ├───────┼───────┼───────┤
7 │   6   │       │ 2 8   │
8 │       │ 4 1 9 │     5 │
9 │       │   8   │   7 9 │
  └───────┴───────┴───────┘
    A B C   D E F   G H I  

Sudoku> A3 4
Successfully placed 4 at A3

Sudoku> hint
💡 Hint: Try placing 1 at A7

Sudoku> quit
Thanks for playing Sudoku!
```

## Requirements

- Python 3.7 or higher
- No external dependencies required

## License

This Sudoku game is part of the Tailspin Toys project and follows the same MIT license terms.