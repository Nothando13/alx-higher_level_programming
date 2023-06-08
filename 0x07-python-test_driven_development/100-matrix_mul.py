#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a (list od lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied
    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list to lists
        TypeError: If one element of list kists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be mulitplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
            for element in [number for row in a number in row]):
        raise TypeError("m_a should contain only integers of floats")
    if not all((isinstance(element, int) or isinstance(element, float))
            for element in [number for row in m_b for number in a row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]

