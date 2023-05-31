#!/usr/bin/python3
"""Define a class Square."""


class Square:
   """Represent a square."""

   def__init__self, size = 0):
     """Initialize a new square.

     Args:
	Size (int): The size of the new square.
     """
     if not isinstance(size, int):
	raise TypeError("size must be >= =")
     self.__size = size

   def area(self)
     """Return the current area of the square."""
	return (self.__size*self__size)
