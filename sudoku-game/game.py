#!/usr/bin/env python3
"""
Sudoku Game CLI
Command-line interface for the Sudoku game.
"""

import sys
import os
from typing import Optional, Tuple

# Add the current directory to the Python path so we can import sudoku
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sudoku import SudokuGame


class SudokuCLI:
    """Command-line interface for the Sudoku game."""
    
    def __init__(self) -> None:
        """Initialize the Sudoku CLI."""
        self.game = SudokuGame()
        self.running = True
    
    def parse_position(self, position: str) -> Optional[Tuple[int, int]]:
        """
        Parse a position string like 'A1' or '1A' into row, col coordinates.
        
        Args:
            position: Position string (e.g., 'A1', '1A', 'a1')
            
        Returns:
            Optional[Tuple[int, int]]: (row, col) coordinates or None if invalid
        """
        position = position.upper().strip()
        
        if len(position) != 2:
            return None
        
        # Try both formats: A1 and 1A
        if position[0].isalpha() and position[1].isdigit():
            col_char, row_char = position[0], position[1]
        elif position[0].isdigit() and position[1].isalpha():
            row_char, col_char = position[0], position[1]
        else:
            return None
        
        # Convert to 0-based indices
        try:
            row = int(row_char) - 1
            col = ord(col_char) - ord('A')
            
            if 0 <= row <= 8 and 0 <= col <= 8:
                return (row, col)
        except ValueError:
            pass
        
        return None
    
    def display_help(self) -> None:
        """Display help information."""
        help_text = """
        Sudoku Game Commands:
        
        Game Commands:
        - new [easy|medium|hard]  : Start a new game with specified difficulty
        - solve                   : Show the complete solution
        - hint                    : Get a hint for the next move
        - quit                    : Exit the game
        
        Move Commands:
        - <position> <number>     : Place a number (1-9) at position
        - <position> 0           : Clear a position
        
        Position formats: A1, 1A, B2, 2B, etc.
        - Letters A-I represent columns
        - Numbers 1-9 represent rows
        
        Examples:
        - A1 5    : Place 5 at position A1
        - 1A 5    : Place 5 at position A1 (same as above)
        - B2 0    : Clear position B2
        
        """
        print(help_text)
    
    def start_new_game(self, difficulty: str = "medium") -> None:
        """
        Start a new game.
        
        Args:
            difficulty: Game difficulty level
        """
        print(f"Generating new {difficulty} Sudoku puzzle...")
        self.game.generate_puzzle(difficulty)
        print("New game started!")
        print(self.game.display_board())
    
    def process_move_command(self, parts: list[str]) -> bool:
        """
        Process a move command.
        
        Args:
            parts: Command parts [position, number]
            
        Returns:
            bool: True if command was processed successfully
        """
        if len(parts) != 2:
            print("Invalid move format. Use: <position> <number>")
            print("Example: A1 5 (place 5 at A1)")
            return False
        
        position_str, number_str = parts
        
        # Parse position
        position = self.parse_position(position_str)
        if position is None:
            print(f"Invalid position: {position_str}")
            print("Use format like A1, B2, etc. (columns A-I, rows 1-9)")
            return False
        
        # Parse number
        try:
            number = int(number_str)
            if not (0 <= number <= 9):
                print("Number must be between 0 (clear) and 9")
                return False
        except ValueError:
            print(f"Invalid number: {number_str}")
            return False
        
        # Make the move
        row, col = position
        if self.game.make_move(row, col, number):
            action = "cleared" if number == 0 else f"placed {number}"
            print(f"Successfully {action} at {position_str.upper()}")
            print(self.game.display_board())
            
            if self.game.is_complete():
                print("🎉 Congratulations! You solved the puzzle! 🎉")
            
            return True
        else:
            if number == 0:
                print(f"Cannot clear position {position_str.upper()}")
            else:
                print(f"Invalid move: cannot place {number} at {position_str.upper()}")
                print("This would violate Sudoku rules (row, column, or box conflict)")
            return False
    
    def run(self) -> None:
        """Run the main game loop."""
        print("=" * 50)
        print("🧩 Welcome to Sudoku! 🧩")
        print("=" * 50)
        print("Type 'help' for commands or 'new' to start a game")
        
        while self.running:
            try:
                command = input("\nSudoku> ").strip().lower()
                
                if not command:
                    continue
                
                parts = command.split()
                main_command = parts[0]
                
                if main_command == "quit" or main_command == "exit":
                    print("Thanks for playing Sudoku!")
                    self.running = False
                
                elif main_command == "help":
                    self.display_help()
                
                elif main_command == "new":
                    difficulty = parts[1] if len(parts) > 1 else "medium"
                    if difficulty not in ["easy", "medium", "hard"]:
                        print(f"Invalid difficulty: {difficulty}")
                        print("Available difficulties: easy, medium, hard")
                    else:
                        self.start_new_game(difficulty)
                
                elif main_command == "solve":
                    if hasattr(self.game, 'solution') and any(any(row) for row in self.game.solution):
                        print("Solution:")
                        # Temporarily show solution
                        original_board = [row[:] for row in self.game.board]
                        self.game.board = [row[:] for row in self.game.solution]
                        print(self.game.display_board())
                        self.game.board = original_board
                        print("Current puzzle:")
                        print(self.game.display_board())
                    else:
                        print("No puzzle is currently loaded. Start a new game first.")
                
                elif main_command == "hint":
                    hint = self.game.get_hint()
                    if hint:
                        row, col, number = hint
                        col_letter = chr(ord('A') + col)
                        print(f"💡 Hint: Try placing {number} at {col_letter}{row + 1}")
                    else:
                        print("No hints available. The puzzle might be complete!")
                
                else:
                    # Try to parse as a move command
                    if len(parts) >= 2:
                        self.process_move_command(parts)
                    else:
                        print(f"Unknown command: {main_command}")
                        print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                self.running = False
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Type 'help' for available commands")


def main() -> None:
    """Main entry point for the Sudoku CLI."""
    cli = SudokuCLI()
    cli.run()


if __name__ == "__main__":
    main()