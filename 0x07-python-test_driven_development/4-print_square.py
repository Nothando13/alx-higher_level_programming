#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #."""

    This function prints a square with the sharacter #
    Args:
        size (int): This represents the length of the square
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    
def print_square(size):
    if not isinstance(size, int):
        raise TypeError: If size is not an integer
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print()    
