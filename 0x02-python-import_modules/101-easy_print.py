# /usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    amalia = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(amalia.keys()):
        print("Unknown operator. Available amalia: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, amalia[sys.argv[2]](a, b)))
