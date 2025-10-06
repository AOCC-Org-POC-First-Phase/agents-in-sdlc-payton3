"""
Base model class for the Tailspin Toys Crowd Funding platform.
This module provides the base functionality for all database models.
"""
from . import db

class BaseModel(db.Model):
    """
    Abstract base model class that provides common functionality for all models.
    
    This class includes validation utilities and should be inherited by all
    database model classes in the application.
    """
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name: str, value: str, min_length: int = 2, allow_none: bool = False) -> str:
        """
        Validate string length for model fields.
        
        Args:
            field_name (str): Name of the field being validated for error messages
            value (str): The string value to validate
            min_length (int, optional): Minimum required length. Defaults to 2.
            allow_none (bool, optional): Whether None values are allowed. Defaults to False.
            
        Returns:
            str: The validated string value
            
        Raises:
            ValueError: If validation fails (empty/None when not allowed, wrong type, too short)
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value