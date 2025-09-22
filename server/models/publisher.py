"""
Publisher model for the Tailspin Toys Crowd Funding platform.
This module defines the Publisher database model for game publishers.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Publisher model representing game publishers in the crowdfunding platform.
    
    A publisher is a company or individual who publishes games.
    Each publisher can have multiple games associated with them.
    
    Attributes:
        id (int): Primary key identifier
        name (str): Publisher name (unique, 2-100 characters)
        description (str): Publisher description (optional, min 10 characters)
        games (List[Game]): List of games published by this publisher
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate publisher name field.
        
        Args:
            key (str): The field name being validated
            name (str): The publisher name to validate
            
        Returns:
            str: The validated publisher name
            
        Raises:
            ValueError: If name is invalid (too short, empty, wrong type)
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key: str, description: str) -> str:
        """
        Validate publisher description field.
        
        Args:
            key (str): The field name being validated
            description (str): The publisher description to validate
            
        Returns:
            str: The validated publisher description
            
        Raises:
            ValueError: If description is invalid (too short when provided)
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self) -> str:
        """
        String representation of the Publisher model.
        
        Returns:
            str: Human-readable representation of the publisher
        """
        return f'<Publisher {self.name}>'

    def to_dict(self) -> dict:
        """
        Convert Publisher model to dictionary representation.
        
        Returns:
            dict: Dictionary containing publisher data with keys:
                - id: Publisher ID
                - name: Publisher name
                - description: Publisher description  
                - game_count: Number of games published by this publisher
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }