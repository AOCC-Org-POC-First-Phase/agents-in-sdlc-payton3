"""
Unit tests for the Sudoku game implementation.
Tests should create shared data at the top to be used for the tests below.
"""

import unittest
import sys
import os

# Add parent directory to path to import sudoku module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sudoku import SudokuGame


class TestSudokuGame(unittest.TestCase):
    """Unit tests for the SudokuGame class."""
    
    # Shared test data
    VALID_PUZZLE = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    COMPLETE_SOLUTION = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.game = SudokuGame()
    
    def tearDown(self) -> None:
        """Clean up after each test method."""
        self.game = None
    
    def test_init(self) -> None:
        """Test game initialization."""
        self.assertIsInstance(self.game.board, list)
        self.assertEqual(len(self.game.board), 9)
        for row in self.game.board:
            self.assertEqual(len(row), 9)
            for cell in row:
                self.assertEqual(cell, 0)
    
    def test_is_valid_move_success(self) -> None:
        """Test valid move detection for success cases."""
        # Test on empty board
        self.assertTrue(self.game.is_valid_move(0, 0, 1))
        self.assertTrue(self.game.is_valid_move(4, 4, 5))
        self.assertTrue(self.game.is_valid_move(8, 8, 9))
        
        # Set up a partial board
        self.game.board = [row[:] for row in self.VALID_PUZZLE]
        
        # Test valid moves
        self.assertTrue(self.game.is_valid_move(0, 2, 4))  # Empty cell, valid number
        self.assertTrue(self.game.is_valid_move(2, 0, 1))  # Empty cell, valid number
    
    def test_is_valid_move_failure(self) -> None:
        """Test valid move detection for failure cases."""
        self.game.board = [row[:] for row in self.VALID_PUZZLE]
        
        # Test invalid moves - row conflict
        self.assertFalse(self.game.is_valid_move(0, 2, 5))  # 5 already in row 0
        
        # Test invalid moves - column conflict
        self.assertFalse(self.game.is_valid_move(2, 0, 6))  # 6 already in column 0
        
        # Test invalid moves - box conflict
        self.assertFalse(self.game.is_valid_move(0, 2, 9))  # 9 already in top-left box
    
    def test_make_move_success(self) -> None:
        """Test successful move execution."""
        # Valid move
        self.assertTrue(self.game.make_move(0, 0, 1))
        self.assertEqual(self.game.board[0][0], 1)
        
        # Clear move
        self.assertTrue(self.game.make_move(0, 0, 0))
        self.assertEqual(self.game.board[0][0], 0)
    
    def test_make_move_failure(self) -> None:
        """Test failed move execution."""
        # Set up a board with conflicts
        self.game.board[0][0] = 1
        
        # Invalid position
        self.assertFalse(self.game.make_move(-1, 0, 1))
        self.assertFalse(self.game.make_move(0, 9, 1))
        
        # Invalid number
        self.assertFalse(self.game.make_move(0, 1, 10))
        self.assertFalse(self.game.make_move(0, 1, -1))
        
        # Rule violation
        self.assertFalse(self.game.make_move(0, 1, 1))  # Same row conflict
    
    def test_solve_solvable_puzzle(self) -> None:
        """Test solving a valid puzzle."""
        self.game.board = [row[:] for row in self.VALID_PUZZLE]
        self.assertTrue(self.game.solve())
        
        # Verify solution is complete and valid
        self.assertTrue(self.game.is_complete())
    
    def test_solve_unsolvable_puzzle(self) -> None:
        """Test solving an unsolvable puzzle."""
        # Create an impossible puzzle with contradictory constraints
        # Fill the entire first row with 1s (impossible)
        for i in range(9):
            self.game.board[0][i] = 1
        
        self.assertFalse(self.game.solve())
    
    def test_is_complete_success(self) -> None:
        """Test completion detection for solved puzzles."""
        self.game.board = [row[:] for row in self.COMPLETE_SOLUTION]
        self.assertTrue(self.game.is_complete())
    
    def test_is_complete_failure(self) -> None:
        """Test completion detection for incomplete puzzles."""
        # Empty board
        self.assertFalse(self.game.is_complete())
        
        # Partially filled board
        self.game.board = [row[:] for row in self.VALID_PUZZLE]
        self.assertFalse(self.game.is_complete())
        
        # Completed but invalid board
        invalid_complete = [row[:] for row in self.COMPLETE_SOLUTION]
        invalid_complete[0][1] = invalid_complete[0][0]  # Create duplicate
        self.game.board = invalid_complete
        self.assertFalse(self.game.is_complete())
    
    def test_generate_puzzle_different_difficulties(self) -> None:
        """Test puzzle generation with different difficulty levels."""
        difficulties = ["easy", "medium", "hard"]
        
        for difficulty in difficulties:
            with self.subTest(difficulty=difficulty):
                self.game.generate_puzzle(difficulty)
                
                # Check that we have a valid puzzle
                self.assertIsNotNone(self.game.board)
                self.assertEqual(len(self.game.board), 9)
                
                # Check that solution exists and is complete
                self.assertTrue(hasattr(self.game, 'solution'))
                
                # Count empty cells to verify difficulty
                empty_cells = sum(row.count(0) for row in self.game.board)
                self.assertGreater(empty_cells, 30)  # Should have reasonable number of empty cells
                self.assertLess(empty_cells, 70)     # Should not be too empty
    
    def test_get_hint_with_solution(self) -> None:
        """Test hint generation when solution is available."""
        self.game.board = [row[:] for row in self.VALID_PUZZLE]
        self.game.solution = [row[:] for row in self.COMPLETE_SOLUTION]
        
        hint = self.game.get_hint()
        self.assertIsNotNone(hint)
        
        row, col, num = hint
        self.assertEqual(self.game.board[row][col], 0)  # Should be empty cell
        self.assertEqual(self.game.solution[row][col], num)  # Should match solution
    
    def test_get_hint_no_empty_cells(self) -> None:
        """Test hint generation when no empty cells exist."""
        self.game.board = [row[:] for row in self.COMPLETE_SOLUTION]
        
        hint = self.game.get_hint()
        self.assertIsNone(hint)
    
    def test_display_board_format(self) -> None:
        """Test board display formatting."""
        display = self.game.display_board()
        
        # Check that display contains expected elements
        self.assertIn("┌", display)  # Top border
        self.assertIn("┐", display)  # Top border
        self.assertIn("└", display)  # Bottom border
        self.assertIn("┘", display)  # Bottom border
        self.assertIn("A B C", display)  # Column labels
        self.assertIn("D E F", display)  # Column labels
        self.assertIn("G H I", display)  # Column labels
        
        # Check row numbers are present
        for i in range(1, 10):
            self.assertIn(str(i), display)


class TestSudokuGameIntegration(unittest.TestCase):
    """Integration tests for complete game workflows."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.game = SudokuGame()
    
    def tearDown(self) -> None:
        """Clean up after tests."""
        self.game = None
    
    def test_full_game_workflow(self) -> None:
        """Test a complete game from generation to completion."""
        # Generate puzzle
        self.game.generate_puzzle("easy")
        
        # Verify puzzle is generated
        self.assertFalse(self.game.is_complete())
        
        # Get original empty cells
        original_empty_cells = [(r, c) for r in range(9) for c in range(9) 
                              if self.game.board[r][c] == 0]
        
        # Fill puzzle with solution
        for row, col in original_empty_cells:
            if hasattr(self.game, 'solution'):
                correct_number = self.game.solution[row][col]
                self.assertTrue(self.game.make_move(row, col, correct_number))
        
        # Verify completion
        self.assertTrue(self.game.is_complete())
    
    def test_puzzle_uniqueness(self) -> None:
        """Test that generated puzzles are different."""
        self.game.generate_puzzle("medium")
        first_puzzle = [row[:] for row in self.game.board]
        
        self.game.generate_puzzle("medium")
        second_puzzle = [row[:] for row in self.game.board]
        
        # Puzzles should be different (very high probability)
        self.assertNotEqual(first_puzzle, second_puzzle)


if __name__ == '__main__':
    unittest.main()