"""
Games API routes for the Tailspin Toys Crowd Funding platform.
This module provides endpoints for retrieving game information.
"""
from flask import jsonify, Response, Blueprint
from models import db, Game, Publisher, Category
from sqlalchemy.orm import Query

# Create a Blueprint for games routes
games_bp = Blueprint('games', __name__)

def get_games_base_query() -> Query:
    """
    Create the base query for retrieving games with related publisher and category data.
    
    This function creates a SQLAlchemy query that joins games with their associated
    publisher and category information using outer joins to handle cases where
    relationships might be None.
    
    Returns:
        Query: SQLAlchemy query object for games with joined publisher and category data
    """
    return db.session.query(Game).join(
        Publisher, 
        Game.publisher_id == Publisher.id, 
        isouter=True
    ).join(
        Category, 
        Game.category_id == Category.id, 
        isouter=True
    )

@games_bp.route('/api/games', methods=['GET'])
def get_games() -> Response:
    """
    Retrieve all games from the database.
    
    This endpoint returns a list of all games in the crowdfunding platform,
    including their associated publisher and category information.
    
    Returns:
        Response: JSON response containing an array of game objects
    """
    # Use the base query for all games
    games_query = get_games_base_query().all()
    
    # Convert the results using the model's to_dict method
    games_list = [game.to_dict() for game in games_query]
    
    return jsonify(games_list)

@games_bp.route('/api/games/<int:id>', methods=['GET'])
def get_game(id: int) -> tuple[Response, int] | Response:
    """
    Retrieve a specific game by ID.
    
    This endpoint returns detailed information about a single game,
    including its associated publisher and category information.
    
    Args:
        id (int): The unique identifier of the game to retrieve
        
    Returns:
        Response: JSON response containing the game object, or 404 error if not found
    """
    # Use the base query and add filter for specific game
    game_query = get_games_base_query().filter(Game.id == id).first()
    
    # Return 404 if game not found
    if not game_query: 
        return jsonify({"error": "Game not found"}), 404
    
    # Convert the result using the model's to_dict method
    game = game_query.to_dict()
    
    return jsonify(game)
