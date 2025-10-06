"""
Sudoku Game Implementation
A complete Sudoku game with puzzle generation, validation, and solving capabilities.
"""

import random
from typing import List, Tuple, Optional


class SudokuGame:
    """A complete Sudoku game implementation with generation and validation."""
    
    def __init__(self) -> None:
        """Initialize a new Sudoku game instance."""
        self.board: List[List[int]] = [[0 for _ in range(9)] for _ in range(9)]
        self.solution: List[List[int]] = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """
        Check if placing a number at the given position is valid.
        
        Args:
            row: Row position (0-8)
            col: Column position (0-8)
            num: Number to place (1-9)
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        # Check row
        for c in range(9):
            if self.board[row][c] == num:
                return False
        
        # Check column
        for r in range(9):
            if self.board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.board[r][c] == num:
                    return False
        
        return True
    
    def solve(self, board: Optional[List[List[int]]] = None) -> bool:
        """
        Solve the Sudoku puzzle using backtracking algorithm.
        
        Args:
            board: Optional board to solve. Uses self.board if not provided.
            
        Returns:
            bool: True if puzzle is solvable, False otherwise
        """
        if board is None:
            board = self.board
            
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self._is_valid_for_board(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    def _is_valid_for_board(self, board: List[List[int]], row: int, col: int, num: int) -> bool:
        """
        Check if placing a number at the given position is valid for a specific board.
        
        Args:
            board: The board to check against
            row: Row position (0-8)
            col: Column position (0-8)
            num: Number to place (1-9)
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False
        
        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        
        return True
    
    def generate_puzzle(self, difficulty: str = "medium") -> None:
        """
        Generate a new Sudoku puzzle.
        
        Args:
            difficulty: Difficulty level ("easy", "medium", "hard")
        """
        # Clear the board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
        # Fill the diagonal 3x3 boxes first
        self._fill_diagonal_boxes()
        
        # Fill the rest of the board
        self.solve()
        
        # Copy the solution
        self.solution = [row[:] for row in self.board]
        
        # Remove numbers based on difficulty
        cells_to_remove = {"easy": 40, "medium": 50, "hard": 60}
        remove_count = cells_to_remove.get(difficulty, 50)
        
        self._remove_numbers(remove_count)
    
    def _fill_diagonal_boxes(self) -> None:
        """Fill the three diagonal 3x3 boxes."""
        for box in range(3):
            self._fill_box(box * 3, box * 3)
    
    def _fill_box(self, row: int, col: int) -> None:
        """
        Fill a 3x3 box with random numbers.
        
        Args:
            row: Starting row of the box
            col: Starting column of the box
        """
        nums = list(range(1, 10))
        random.shuffle(nums)
        
        for i in range(3):
            for j in range(3):
                self.board[row + i][col + j] = nums[i * 3 + j]
    
    def _remove_numbers(self, count: int) -> None:
        """
        Remove numbers from the solved puzzle to create the game.
        
        Args:
            count: Number of cells to remove
        """
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        
        for i in range(min(count, 81)):
            row, col = cells[i]
            self.board[row][col] = 0
    
    def make_move(self, row: int, col: int, num: int) -> bool:
        """
        Make a move on the board.
        
        Args:
            row: Row position (0-8)
            col: Column position (0-8)
            num: Number to place (1-9, or 0 to clear)
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        if not (0 <= row <= 8 and 0 <= col <= 8):
            return False
        
        if num == 0:
            self.board[row][col] = 0
            return True
        
        if not (1 <= num <= 9):
            return False
        
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True
        
        return False
    
    def is_complete(self) -> bool:
        """
        Check if the puzzle is completely solved.
        
        Returns:
            bool: True if puzzle is complete and valid, False otherwise
        """
        # Check if all cells are filled
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        
        # Check if solution is valid
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                self.board[row][col] = 0  # Temporarily remove to check validity
                if not self.is_valid_move(row, col, num):
                    self.board[row][col] = num  # Restore
                    return False
                self.board[row][col] = num  # Restore
        
        return True
    
    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """
        Get a hint for the next move.
        
        Returns:
            Optional[Tuple[int, int, int]]: (row, col, number) for hint, or None if no hint available
        """
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.board[r][c] == 0]
        
        if not empty_cells:
            return None
        
        # Return the first solvable empty cell from the solution
        for row, col in empty_cells:
            if hasattr(self, 'solution') and self.solution[row][col] != 0:
                return (row, col, self.solution[row][col])
        
        return None
    
    def display_board(self) -> str:
        """
        Get a formatted string representation of the board.
        
        Returns:
            str: Formatted board string
        """
        board_str = "\n  ┌───────┬───────┬───────┐\n"
        
        for row in range(9):
            if row == 3 or row == 6:
                board_str += "  ├───────┼───────┼───────┤\n"
            
            board_str += f"{row + 1} │"
            
            for col in range(9):
                if col == 3 or col == 6:
                    board_str += "│"
                
                cell_value = self.board[row][col]
                display_value = str(cell_value) if cell_value != 0 else " "
                board_str += f" {display_value} "
            
            board_str += "│\n"
        
        board_str += "  └───────┴───────┴───────┘\n"
        board_str += "    A B C   D E F   G H I  \n"
        
        return board_str