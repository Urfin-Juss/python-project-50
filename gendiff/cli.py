# cli.py
import argparse


def cli_gendiff():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')

    args = parser.parse_args()

    print(args.first_file)
    print(args.second_file)


if __name__ == '__main__':
    cli_gendiff()