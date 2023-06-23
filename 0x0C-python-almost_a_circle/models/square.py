#!/usr/bin/python3
"""Module that defines a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
	"""Method that initialized the square
	Args:
	   size: side's size of the square
	   x: Position on x axis.
	   y: Position on y axis.
	Return:
