import argparse
import sys


def adder(a, b):
    return a + b


def get_params(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="variable [a]")
    parser.add_argument("b", type=int, help="variable [b]")
    parsed_params = parser.parse_args(args)
    print(f"argparse: {parsed_params= }")
    return parsed_params.a, parsed_params.b


if __name__ == "__main__":
    a, b = get_params(sys.argv[1:])
    print(f"calculate {a} + {b} = {adder(a, b)}")
