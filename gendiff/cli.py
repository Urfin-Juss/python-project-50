# cli.py

import argparse

from gendiff.core.diff_json import generate_diff_json


def cli_gendiff():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    format_choices = ["FORMAT"]
    parser.add_argument(
        "-f",
        "--format",
        choices=format_choices,
        default=None,
        help="set format of output",
    )

    args = parser.parse_args()

    print(args.first_file)
    print(args.second_file)

    print(generate_diff_json(args.first_file, args.second_file))


if __name__ == "__main__":
    cli_gendiff()
