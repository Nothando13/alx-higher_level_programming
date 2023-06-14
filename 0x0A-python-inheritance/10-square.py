#!/usr/bin/python3
"""Class definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """super class"""

    def __init__ initialise new square

    Args:
            integer size of new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
