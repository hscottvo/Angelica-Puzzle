import random
from argparse import ArgumentParser, ArgumentTypeError, FileType

import game
import search

parser = ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument(
    "--heuristic",
    help="1 for uniform cost, 2 for misplaced tile, 3 for manhattan distance",
    type=int,
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-r",
    "--random",
    help="how many random moves to make to start the puzzle in",
    type=int,
)
group.add_argument("-f", "--file", type=FileType("r"))

heuristics = {1: "uniform_cost", 2: "misplaced_tile", 3: "manhattan"}


def main():
    args = parser.parse_args()

    if args.heuristic not in heuristics:
        raise TypeError(f"Got heuristic key {args.heuristic}. Must be in range [1, 3]")

    if args.file is None:
        game_to_solve = game.Game(
            heuristic=heuristics[args.heuristic], verbose=args.verbose
        )
        for i in range(args.random):
            new_game = game_to_solve.move(random.choice(list(game.Move)))
            if new_game is not None:
                game_to_solve = new_game
            else:
                i -= 1
        game_to_solve.reset()
        search.search(game_to_solve, verbose=args.verbose)
    else:
        lines = [i.strip() for i in args.file.readlines()]
        matrix = [i.replace("0", "\u25a1").split() for i in lines]
        search.search(
            game.Game(
                matrix,
                heuristic=heuristics[args.heuristic],
                verbose=args.verbose,
            ),
            verbose=args.verbose,
        )

    return


if __name__ == "__main__":
    main()
