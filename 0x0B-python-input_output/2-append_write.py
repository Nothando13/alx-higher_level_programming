#!/usr/bin/python3


def append_write(filename=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
