import argparse
import sys


def adder_list(param_list):
    return sum(param_list)


def get_params(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("int_list", type=int, nargs="+", help="a list of integers")
    parsed_params = parser.parse_args(args[1:])
    print(f"argparse: {parsed_params= }")
    return parsed_params.int_list


if __name__ == "__main__":
    params = get_params(sys.argv)
    print(f"calculate {params} = {adder_list(param_list=params)}")
