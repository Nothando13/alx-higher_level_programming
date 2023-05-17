#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()

argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    func = add        
elif (argv[1] == "-"):
    func = sub
elif (argv[1] == "*"):
    func = mul
elif (argv[1] == "/"):
    func = div
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

result = func(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d}".format(int(argv[1]),
    srgv[2], int(argv[3]), result))
