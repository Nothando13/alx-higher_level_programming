#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
=================================
Module with class Rectangle
=================================
"""



class Rectangle(BaseGeometry):
    """create new class instance."""

    def __int__self, width, height):
        """Intialize a new Rectangle instance

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
