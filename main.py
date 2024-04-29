from argparse import ArgumentParser

import game
import search

parser = ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument(
    "-r",
    "--random",
    help="how many random moves to make to start the puzzle in",
    type=int,
)


def main():
    print(parser.parse_args().verbose)
    return


if __name__ == "__main__":
    main()
