"""
Category model for the Tailspin Toys Crowd Funding platform.
This module defines the Category database model for organizing games.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """
    Category model representing game categories in the crowdfunding platform.
    
    A category groups related games together (e.g., Strategy, RPG, Action).
    Each category can have multiple games associated with it.
    
    Attributes:
        id (int): Primary key identifier
        name (str): Category name (unique, 2-100 characters)  
        description (str): Category description (optional, min 10 characters)
        games (List[Game]): List of games in this category
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate category name field.
        
        Args:
            key (str): The field name being validated
            name (str): The category name to validate
            
        Returns:
            str: The validated category name
            
        Raises:
            ValueError: If name is invalid (too short, empty, wrong type)
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key: str, description: str) -> str:
        """
        Validate category description field.
        
        Args:
            key (str): The field name being validated  
            description (str): The category description to validate
            
        Returns:
            str: The validated category description
            
        Raises:
            ValueError: If description is invalid (too short when provided)
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self) -> str:
        """
        String representation of the Category model.
        
        Returns:
            str: Human-readable representation of the category
        """
        return f'<Category {self.name}>'
        
    def to_dict(self) -> dict:
        """
        Convert Category model to dictionary representation.
        
        Returns:
            dict: Dictionary containing category data with keys:
                - id: Category ID
                - name: Category name  
                - description: Category description
                - game_count: Number of games in this category
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }