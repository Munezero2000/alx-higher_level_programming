#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if len((sys.argv) - 1) != 3:
        print(" Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif len((sys.argv) - 1) == 3 and sys.argv[2] == "+":
        print("{} {} {}= {}".format(a, sys.argv[2], b,
                                    add(a, b)))
    elif len((sys.argv) - 1) == 3 and sys.argv[2] == "-":
        print("{} + {} = {}".format(a, sys.argv[2], b,
                                    add(a, b)))
    elif len((sys.argv) - 1) == 3 and sys.argv[2] == "*":
        print("{} + {} = {}".format(a, sys.argv[2], b,
                                    add(a, b)))
    elif len((sys.argv) - 1) == 3 and sys.argv[2] == "/":
        print("{} + {} = {}".format(a, sys.argv[2], b,
                                    add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
