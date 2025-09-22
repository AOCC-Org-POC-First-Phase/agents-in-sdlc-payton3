"""
Game model for the Tailspin Toys Crowd Funding platform.
This module defines the Game database model for games seeking crowdfunding.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Game(BaseModel):
    """
    Game model representing games in the crowdfunding platform.
    
    A game is the main entity that users can browse and support through crowdfunding.
    Each game belongs to a category and is published by a publisher.
    
    Attributes:
        id (int): Primary key identifier
        title (str): Game title (2-100 characters)
        description (str): Game description (min 10 characters)
        star_rating (float): Star rating (optional, 0.0-5.0)
        category_id (int): Foreign key to categories table
        publisher_id (int): Foreign key to publishers table
        category (Category): Associated category object
        publisher (Publisher): Associated publisher object
    """
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Float, nullable=True)
    
    # Foreign keys for one-to-many relationships
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    
    # One-to-many relationships (many games belong to one category/publisher)
    category = relationship("Category", back_populates="games")
    publisher = relationship("Publisher", back_populates="games")
    
    @validates('title')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate game title field.
        
        Args:
            key (str): The field name being validated
            name (str): The game title to validate
            
        Returns:
            str: The validated game title
            
        Raises:
            ValueError: If title is invalid (too short, empty, wrong type)
        """
        return self.validate_string_length('Game title', name, min_length=2)
    
    @validates('description')
    def validate_description(self, key: str, description: str) -> str:
        """
        Validate game description field.
        
        Args:
            key (str): The field name being validated
            description (str): The game description to validate
            
        Returns:
            str: The validated game description
            
        Raises:
            ValueError: If description is invalid (too short when provided)
        """
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    def __repr__(self) -> str:
        """
        String representation of the Game model.
        
        Returns:
            str: Human-readable representation of the game
        """
        return f'<Game {self.title}, ID: {self.id}>'

    def to_dict(self) -> dict:
        """
        Convert Game model to dictionary representation.
        
        Returns:
            dict: Dictionary containing game data with keys:
                - id: Game ID
                - title: Game title
                - description: Game description
                - publisher: Publisher object (id, name) or None
                - category: Category object (id, name) or None
                - starRating: Star rating (camelCase for frontend)
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publisher': {'id': self.publisher.id, 'name': self.publisher.name} if self.publisher else None,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None,
            'starRating': self.star_rating  # Changed from star_rating to starRating
        }