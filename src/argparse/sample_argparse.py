import argparse
import sys


def adder(a, b):
    return a + b


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_file",
        metavar="path",
        type=str,
        default="soup.yaml",
        help="YAML input file path",
    )
    parser.add_argument(
        "output_folder",
        metavar="path",
        type=str,
        default="./soup",
        help="output folder path",
    )
    parser.add_argument(
        "--replace", action="store_true", default=False, help="True if always replace"
    )
    parser.add_argument(
        "--retry", action="store_true", default=False, help="True if require retry"
    )
    parser.add_argument(
        "--no_file_index",
        action="store_true",
        default=False,
        help="True if require retry",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        default=False,
        help="True if want to start from first image",
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(f"calculate {a} + {b} = {adder(a, b)}")
