#!/usr/bin/python3


def no_c(my_string):
    valstore = []
    for x in my_string:
        if x != "c" and x != "C":
            valstore.append(x)
            print("".join(valstore))
