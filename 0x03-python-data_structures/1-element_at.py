#!/usr/bin/python3
<<<<<<< HEAD
def element_at(my_list, idx):
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")
=======

def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
>>>>>>> ffdd96fbd78609e11136213d5dad2e112d69e95e
