"""
Database initialization utilities for the Tailspin Toys Crowd Funding platform.
This module provides functions to initialize the database connection and configuration.
"""
import os
from models import init_db as models_init_db

def init_db(app, connection_string: str = None, testing: bool = False) -> None:
    """
    Initialize the database with the given Flask app and connection string.
    
    If no connection string is provided, a default SQLite connection string is used.
    
    Args:
        app: The Flask application instance
        connection_string (str, optional): Database connection string. Defaults to None.
        testing (bool, optional): If True, allows reinitialization for testing. Defaults to False.
    """
    if connection_string is None:
        connection_string = __get_connection_string()
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    models_init_db(app, testing=testing)

def __get_connection_string() -> str:
    """
    Get the connection string for the database.
    
    This function constructs a SQLite database connection string pointing to 
    the tailspin-toys.db file in the data directory. It creates the data
    directory if it doesn't exist.
    
    Returns:
        str: SQLite connection string for the database
    """
    # Get the server directory
    server_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(server_dir)
    data_dir = os.path.join(project_root, "data")
    
    # Create the data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    return f'sqlite:///{os.path.join(data_dir, "tailspin-toys.db")}'