"""
Sudoku API routes for the Tailspin Toys Crowd Funding platform.
This module provides endpoints for the Sudoku game functionality.
"""

from flask import Blueprint, jsonify, request
import sys
import os

# Add the sudoku-game directory to the Python path
sudoku_game_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'sudoku-game')
sys.path.insert(0, sudoku_game_path)

from sudoku import SudokuGame

# Create blueprint
sudoku_bp = Blueprint('sudoku', __name__, url_prefix='/api/sudoku')

# Global game instances for session management (in production, use proper session management)
game_sessions = {}


@sudoku_bp.route('/new', methods=['POST'])
def create_new_game():
    """
    Create a new Sudoku game with specified difficulty.
    
    Returns:
        Response: JSON response containing the new game board and session ID
    """
    try:
        # Handle case where no JSON data is provided
        try:
            data = request.get_json()
            if data is None:
                data = {}
        except:
            data = {}
            
        difficulty = data.get('difficulty', 'medium')
        
        if difficulty not in ['easy', 'medium', 'hard']:
            return jsonify({'error': 'Invalid difficulty. Choose from: easy, medium, hard'}), 400
        
        # Create new game
        game = SudokuGame()
        game.generate_puzzle(difficulty)
        
        # Generate a simple session ID (in production, use proper session management)
        session_id = f"game_{len(game_sessions)}"
        game_sessions[session_id] = game
        
        return jsonify({
            'session_id': session_id,
            'board': game.board,
            'difficulty': difficulty,
            'message': f'New {difficulty} Sudoku puzzle generated successfully'
        }), 201
        
    except Exception as e:
        return jsonify({'error': f'Failed to create game: {str(e)}'}), 500


@sudoku_bp.route('/move', methods=['POST'])
def make_move():
    """
    Make a move on the Sudoku board.
    
    Returns:
        Response: JSON response with move result and updated board state
    """
    try:
        try:
            data = request.get_json()
        except:
            data = None
            
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        session_id = data.get('session_id')
        row = data.get('row')
        col = data.get('col')
        num = data.get('num')
        
        if row is None or col is None or num is None:
            return jsonify({'error': 'Missing required fields: row, col, num'}), 400
        
        if not session_id or session_id not in game_sessions:
            return jsonify({'error': 'Invalid or expired game session'}), 404
        
        if not (0 <= row <= 8 and 0 <= col <= 8 and 0 <= num <= 9):
            return jsonify({'error': 'Invalid coordinates or number'}), 400
        
        game = game_sessions[session_id]
        
        # Make the move
        success = game.make_move(row, col, num)
        
        if success:
            is_complete = game.is_complete()
            action = "cleared" if num == 0 else f"placed {num}"
            
            return jsonify({
                'success': True,
                'board': game.board,
                'message': f'Successfully {action} at position ({row + 1}, {chr(ord("A") + col)})',
                'is_complete': is_complete
            }), 200
        else:
            return jsonify({
                'success': False,
                'board': game.board,
                'message': 'Invalid move: would violate Sudoku rules'
            }), 400
        
    except Exception as e:
        return jsonify({'error': f'Failed to make move: {str(e)}'}), 500


@sudoku_bp.route('/hint', methods=['POST'])
def get_hint():
    """
    Get a hint for the current puzzle.
    
    Returns:
        Response: JSON response with hint information
    """
    try:
        try:
            data = request.get_json()
        except:
            data = None
            
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        session_id = data.get('session_id')
        
        if not session_id or session_id not in game_sessions:
            return jsonify({'error': 'Invalid or expired game session'}), 404
        
        game = game_sessions[session_id]
        hint = game.get_hint()
        
        if hint:
            row, col, num = hint
            col_letter = chr(ord('A') + col)
            return jsonify({
                'hint': True,
                'row': row,
                'col': col,
                'num': num,
                'message': f'Try placing {num} at {col_letter}{row + 1}'
            }), 200
        else:
            return jsonify({
                'hint': False,
                'message': 'No hints available. The puzzle might be complete!'
            }), 200
            
    except Exception as e:
        return jsonify({'error': f'Failed to get hint: {str(e)}'}), 500


@sudoku_bp.route('/solve', methods=['POST'])
def solve_puzzle():
    """
    Show the complete solution for the current puzzle.
    
    Returns:
        Response: JSON response with the complete solution
    """
    try:
        try:
            data = request.get_json()
        except:
            data = None
            
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        session_id = data.get('session_id')
        
        if not session_id or session_id not in game_sessions:
            return jsonify({'error': 'Invalid or expired game session'}), 404
        
        game = game_sessions[session_id]
        
        if hasattr(game, 'solution') and any(any(row) for row in game.solution):
            return jsonify({
                'solution': game.solution,
                'current_board': game.board,
                'message': 'Complete solution displayed'
            }), 200
        else:
            return jsonify({'error': 'No solution available for current puzzle'}), 404
            
    except Exception as e:
        return jsonify({'error': f'Failed to get solution: {str(e)}'}), 500


@sudoku_bp.route('/status', methods=['POST'])
def get_game_status():
    """
    Get the current status of a game session.
    
    Returns:
        Response: JSON response with current game state
    """
    try:
        try:
            data = request.get_json()
        except:
            data = None
            
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        session_id = data.get('session_id')
        
        if not session_id or session_id not in game_sessions:
            return jsonify({'error': 'Invalid or expired game session'}), 404
        
        game = game_sessions[session_id]
        
        empty_cells = sum(row.count(0) for row in game.board)
        is_complete = game.is_complete()
        
        return jsonify({
            'board': game.board,
            'empty_cells': empty_cells,
            'is_complete': is_complete,
            'message': 'Puzzle completed!' if is_complete else f'{empty_cells} cells remaining'
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Failed to get game status: {str(e)}'}), 500