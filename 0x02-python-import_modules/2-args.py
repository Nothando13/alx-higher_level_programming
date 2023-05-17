#!/usr/bin/python3
<<<<<<< HEAD
import sys
if _name_ == "_main_":
=======
if __name__ == "__main__":
    import sys
>>>>>>> ce1f2076fd923ab1b811d47413e6fb12ea4b7125

    sys.argv.pop(0)
    argvlength = len(sys.argv)

    if (argvlength == 0:
        print("0 arguments.")
    elif (argvlength == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv[0]))
    else:
        print("{:d} arguments:".format(argvlength))
        number = 1
    for argument in sys.argv:
            print("{:d}:. {}".format(number, argument))
            number += 1
