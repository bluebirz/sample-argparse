import argparse
import sys


def adder_list(param_list):
    return sum(param_list)


def multiplier_list(param_list):
    product = 1
    for param in param_list:
        product *= param
    return product


def get_params(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("int_list", type=int, nargs="+", help="a list of integers")
    parser.add_argument(
        "--ops",
        "-o",
        type=str,
        choices=["add", "mult"],
        help="An operator to perform with",
    )
    parsed_params = parser.parse_args(args[1:])
    print(f"argparse: {parsed_params= }")
    return parsed_params.int_list, parsed_params.ops


if __name__ == "__main__":
    params, ops = get_params(sys.argv)
    if ops == "add":
        print(f"calculate {params} with 'add'  = {adder_list(param_list=params)}")
    else:
        print(f"calculate {params} with 'mult'  = {multiplier_list(param_list=params)}")
