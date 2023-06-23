#!/usr/bin/python3
from models.base import Base

"""This module defines a class Rectangle tha inherits from Base"""

class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.

    Attributes:
        width (int): width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle's position.
        y (in): Y-coordinate of the rectangle's position.
        id (int): Unique identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
	    x (int, optional): X-coordinate of the rectangle's
	    position. Defaults to 0.
	    y (int, optional): Y-coordinate of the rectangle's
	    position. Defaults to 0.
	    id (int, optional): Unique identifier for the rectangle.
	    Defaults to None.

	Note:
	    The id argument is passed to the super class constructor
	    (Base) using the super() function.
	"""

	super().__init__(id)
	self.width = width
	self.height = height
	self.x = x
	self.y = y
    
    @property
    def width(self):
	"""Set the width of the rectangle."""
	if not isinstance(value, int):
	    raise TypeError("width must be an integer.")
	if value <= 0:
	    raise ValueError("width must be > 0.")
	self.__width = value

    @property
    def width(self):
	"""Get the width of the rectangle."""
	return self.__width

    @width.setter
    def width(self, value):
	"""Set the width of the rectangle."""
	if not isinstance(value, int):
	    raise TypeError("width must be an integer.")
	if value <= 0:
	    raise ValueError("width must be > 0.")
	self.__width = value



