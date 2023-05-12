#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    operator = sys.argv[2]
    if operator not in operators:
        print(operator)
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operation = operators[sys.argv[2]]
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, operation(a, b)))
