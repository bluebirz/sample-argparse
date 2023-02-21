import sys


def adder(a, b):
    return a + b


def get_params(argv):
    a = int(argv[1])
    b = int(argv[2])
    print(f"argparse: {a= }, {b= }")
    return a, b


if __name__ == "__main__":
    a, b = get_params(sys.argv)
    print(f"calculate {a} + {b} = {adder(a, b)}")
