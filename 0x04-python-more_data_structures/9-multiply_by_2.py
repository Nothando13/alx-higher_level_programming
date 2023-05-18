#!/usr/bin/python3
def muliply_by_2(a_dictionary):
    """
    using dictionary comprehension for my first time
    in order to multiply the value of every key: value
    pair in a dictionary
    """
    return {key: vale*2 for (key, value) in a_dictionary.items()}
