"""
Unit tests for the Sudoku API routes.
Tests should create shared data at the top to be used for the tests below.
"""

import unittest
import json
import sys
import os
from io import StringIO

# Add the server directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from routes.sudoku import game_sessions


class TestSudokuRoutes(unittest.TestCase):
    """Unit tests for the Sudoku API routes."""

    # Shared test data
    VALID_SESSION_DATA = {
        'difficulty': 'medium'
    }
    
    INVALID_DIFFICULTY_DATA = {
        'difficulty': 'invalid'
    }
    
    VALID_MOVE_DATA = {
        'row': 0,
        'col': 0,
        'num': 1
    }

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Clear any existing game sessions
        game_sessions.clear()
        
        # Suppress print statements during testing
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self) -> None:
        """Clean up after each test method."""
        # Restore stdout
        sys.stdout = self.held
        
        # Clear game sessions
        game_sessions.clear()

    def test_create_new_game_success(self) -> None:
        """Test successful creation of a new Sudoku game."""
        response = self.client.post('/api/sudoku/new',
                                  json=self.VALID_SESSION_DATA,
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        
        data = json.loads(response.data)
        self.assertIn('session_id', data)
        self.assertIn('board', data)
        self.assertIn('difficulty', data)
        self.assertIn('message', data)
        
        # Verify board structure
        self.assertEqual(len(data['board']), 9)
        for row in data['board']:
            self.assertEqual(len(row), 9)
        
        # Verify difficulty
        self.assertEqual(data['difficulty'], 'medium')
        
        # Verify session was created
        self.assertIn(data['session_id'], game_sessions)

    def test_create_new_game_invalid_difficulty(self) -> None:
        """Test creation of a new game with invalid difficulty."""
        response = self.client.post('/api/sudoku/new',
                                  json=self.INVALID_DIFFICULTY_DATA,
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Invalid difficulty', data['error'])

    def test_create_new_game_no_data(self) -> None:
        """Test creation of a new game with no data (should use default difficulty)."""
        response = self.client.post('/api/sudoku/new',
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        
        data = json.loads(response.data)
        self.assertEqual(data['difficulty'], 'medium')  # Default difficulty

    def test_make_move_success(self) -> None:
        """Test successful move on Sudoku board."""
        # First create a game
        new_game_response = self.client.post('/api/sudoku/new',
                                           json=self.VALID_SESSION_DATA,
                                           content_type='application/json')
        game_data = json.loads(new_game_response.data)
        session_id = game_data['session_id']
        
        # Make a move
        move_data = dict(self.VALID_MOVE_DATA)
        move_data['session_id'] = session_id
        
        response = self.client.post('/api/sudoku/move',
                                  json=move_data,
                                  content_type='application/json')
        
        # The response depends on whether the move is valid for the generated puzzle
        self.assertIn(response.status_code, [200, 400])  # Could be valid or invalid move
        
        data = json.loads(response.data)
        self.assertIn('success', data)
        self.assertIn('board', data)
        self.assertIn('message', data)

    def test_make_move_invalid_session(self) -> None:
        """Test making a move with invalid session ID."""
        move_data = dict(self.VALID_MOVE_DATA)
        move_data['session_id'] = 'invalid_session'
        
        response = self.client.post('/api/sudoku/move',
                                  json=move_data,
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Invalid or expired game session', data['error'])

    def test_make_move_missing_data(self) -> None:
        """Test making a move with missing data."""
        response = self.client.post('/api/sudoku/move',
                                  json={'session_id': 'test'},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Missing required fields', data['error'])

    def test_make_move_invalid_coordinates(self) -> None:
        """Test making a move with invalid coordinates."""
        # First create a game
        new_game_response = self.client.post('/api/sudoku/new',
                                           json=self.VALID_SESSION_DATA,
                                           content_type='application/json')
        game_data = json.loads(new_game_response.data)
        session_id = game_data['session_id']
        
        # Make a move with invalid coordinates
        move_data = {
            'session_id': session_id,
            'row': 10,  # Invalid row
            'col': 0,
            'num': 1
        }
        
        response = self.client.post('/api/sudoku/move',
                                  json=move_data,
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('Invalid coordinates', data['error'])

    def test_get_hint_success(self) -> None:
        """Test getting a hint for the current puzzle."""
        # First create a game
        new_game_response = self.client.post('/api/sudoku/new',
                                           json=self.VALID_SESSION_DATA,
                                           content_type='application/json')
        game_data = json.loads(new_game_response.data)
        session_id = game_data['session_id']
        
        # Get hint
        response = self.client.post('/api/sudoku/hint',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('hint', data)
        self.assertIn('message', data)
        
        if data['hint']:
            self.assertIn('row', data)
            self.assertIn('col', data)
            self.assertIn('num', data)

    def test_get_hint_invalid_session(self) -> None:
        """Test getting a hint with invalid session."""
        response = self.client.post('/api/sudoku/hint',
                                  json={'session_id': 'invalid'},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_solve_puzzle_success(self) -> None:
        """Test showing the solution for current puzzle."""
        # First create a game
        new_game_response = self.client.post('/api/sudoku/new',
                                           json=self.VALID_SESSION_DATA,
                                           content_type='application/json')
        game_data = json.loads(new_game_response.data)
        session_id = game_data['session_id']
        
        # Get solution
        response = self.client.post('/api/sudoku/solve',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        # Should succeed if solution exists
        self.assertIn(response.status_code, [200, 404])
        
        data = json.loads(response.data)
        if response.status_code == 200:
            self.assertIn('solution', data)
            self.assertIn('current_board', data)
            self.assertIn('message', data)
            
            # Verify solution structure
            self.assertEqual(len(data['solution']), 9)
            for row in data['solution']:
                self.assertEqual(len(row), 9)

    def test_solve_puzzle_invalid_session(self) -> None:
        """Test showing solution with invalid session."""
        response = self.client.post('/api/sudoku/solve',
                                  json={'session_id': 'invalid'},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_get_game_status_success(self) -> None:
        """Test getting game status for valid session."""
        # First create a game
        new_game_response = self.client.post('/api/sudoku/new',
                                           json=self.VALID_SESSION_DATA,
                                           content_type='application/json')
        game_data = json.loads(new_game_response.data)
        session_id = game_data['session_id']
        
        # Get status
        response = self.client.post('/api/sudoku/status',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('board', data)
        self.assertIn('empty_cells', data)
        self.assertIn('is_complete', data)
        self.assertIn('message', data)
        
        # Verify data types
        self.assertIsInstance(data['empty_cells'], int)
        self.assertIsInstance(data['is_complete'], bool)

    def test_get_game_status_invalid_session(self) -> None:
        """Test getting status with invalid session."""
        response = self.client.post('/api/sudoku/status',
                                  json={'session_id': 'invalid'},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_api_endpoints_without_data(self) -> None:
        """Test API endpoints when no JSON data is provided."""
        endpoints = ['/api/sudoku/move', '/api/sudoku/hint', '/api/sudoku/solve', '/api/sudoku/status']
        
        for endpoint in endpoints:
            response = self.client.post(endpoint, content_type='application/json')
            self.assertEqual(response.status_code, 400)
            
            data = json.loads(response.data)
            self.assertIn('error', data)
            self.assertIn('No data provided', data['error'])


class TestSudokuIntegration(unittest.TestCase):
    """Integration tests for Sudoku API workflows."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Clear any existing game sessions
        game_sessions.clear()
        
        # Suppress print statements during testing
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self) -> None:
        """Clean up after tests."""
        # Restore stdout
        sys.stdout = self.held
        
        # Clear game sessions
        game_sessions.clear()

    def test_full_game_workflow(self) -> None:
        """Test a complete game workflow from creation to completion."""
        # Step 1: Create new game
        response = self.client.post('/api/sudoku/new',
                                  json={'difficulty': 'easy'},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        game_data = json.loads(response.data)
        session_id = game_data['session_id']
        
        # Step 2: Get initial status
        response = self.client.post('/api/sudoku/status',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        status_data = json.loads(response.data)
        self.assertFalse(status_data['is_complete'])
        self.assertGreater(status_data['empty_cells'], 0)
        
        # Step 3: Try to get a hint
        response = self.client.post('/api/sudoku/hint',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        hint_data = json.loads(response.data)
        self.assertIn('hint', hint_data)
        
        # Step 4: Get solution (if available)
        response = self.client.post('/api/sudoku/solve',
                                  json={'session_id': session_id},
                                  content_type='application/json')
        
        # Solution should be available for generated puzzles
        self.assertIn(response.status_code, [200, 404])

    def test_multiple_game_sessions(self) -> None:
        """Test handling multiple concurrent game sessions."""
        session_ids = []
        
        # Create multiple games
        for difficulty in ['easy', 'medium', 'hard']:
            response = self.client.post('/api/sudoku/new',
                                      json={'difficulty': difficulty},
                                      content_type='application/json')
            
            self.assertEqual(response.status_code, 201)
            game_data = json.loads(response.data)
            session_ids.append(game_data['session_id'])
        
        # Verify all sessions exist and are independent
        for session_id in session_ids:
            response = self.client.post('/api/sudoku/status',
                                      json={'session_id': session_id},
                                      content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            status_data = json.loads(response.data)
            self.assertIn('board', status_data)

    def test_session_persistence(self) -> None:
        """Test that game sessions persist across multiple API calls."""
        # Create game
        response = self.client.post('/api/sudoku/new',
                                  json={'difficulty': 'medium'},
                                  content_type='application/json')
        
        game_data = json.loads(response.data)
        session_id = game_data['session_id']
        original_board = game_data['board']
        
        # Make multiple status calls
        for _ in range(3):
            response = self.client.post('/api/sudoku/status',
                                      json={'session_id': session_id},
                                      content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            status_data = json.loads(response.data)
            
            # Board should remain consistent
            self.assertEqual(status_data['board'], original_board)


if __name__ == '__main__':
    unittest.main()