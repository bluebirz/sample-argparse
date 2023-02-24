import argparse
import sys
import requests
import os


def curl_website(url):
    req = requests.get(url)
    html = req.content
    return html


def save_to_file(filepath, contents):
    with open(filepath, "wb") as fptr:
        fptr.write(contents)


def get_params(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="a target website")
    parser.add_argument(
        "filepath",
        type=str,
        help="a destination filepath",
    )
    parser.add_argument(
        "-w",
        "--overwrite",
        action="store_true",
        help="True to allow overwrite",
    )
    parsed_params = parser.parse_args(args[1:])
    print(f"argparse: {parsed_params= }")
    return parsed_params.url, parsed_params.filepath, parsed_params.overwrite


if __name__ == "__main__":
    url, filepath, is_overwrite = get_params(sys.argv)
    if os.path.isfile(filepath) and not is_overwrite:
        raise FileExistsError
    print(f"reading contents from {url}")
    contents = curl_website(url)
    print(f"saving contents to path {filepath} ({is_overwrite=})")
    save_to_file(filepath, contents)
    print(f"Saved contents to the file")
