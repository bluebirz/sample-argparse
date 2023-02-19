import sys


def adder_list(param_list):
    return sum(param_list)


def get_params(argv):
    params = list(map(int, argv[1:]))
    return params


if __name__ == "__main__":
    params = get_params(sys.argv)
    print(f"calculate {params} = {adder_list(param_list=params)}")
