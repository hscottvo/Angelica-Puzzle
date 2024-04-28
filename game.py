from copy import deepcopy
from enum import Enum
from typing import List, Tuple, Union


class Move(Enum):
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    UP = (-1, 0)


class Game:
    default_state = [["A", "N", "G"], ["E", "L", "I"], ["C", "A", "\u25a1"]]

    def __init__(
        self,
        state: List[List[str]] = default_state,
        empty: str = "\u25a1",
    ):
        self.state = state
        self.empty = empty
        self.solution = [["A", "N", "G"], ["E", "L", "I"], ["C", "A", self.empty]]
        self.__map_solution()
        self.height = len(state)
        assert self.height > 0
        self.width = len(state[0])
        self.__check_size()
        self.__assign_empty()

    def __map_solution(self) -> None:
        """Map each character in the solution to the correct coordinate."""
        self.solution_map = dict()
        for row_idx, row in enumerate(self.solution):
            for col_idx, cell in enumerate(row):
                # needs special attention for A since there are multiple
                if cell == "A":
                    continue
                self.solution_map[cell] = (row_idx, col_idx)
        return

    def __check_size(self):
        """Raises an exception if the game state is not rectangular."""
        for i in self.state:
            if len(i) != self.width:
                raise Exception("Width must be greater than 0!")

    def __assign_empty(self) -> None:
        """Finds the empty tile and records its coordinate."""
        for i in range(self.height):
            for j in range(self.width):
                if self.state[i][j] == self.empty:
                    self.empty_coord = (i, j)

    def __str__(self) -> str:
        """Converts the puzzle state into a string for easy printing."""
        return "\n".join([" ".join([i for i in row]) for row in self.state])

    def move(self, direction: Move) -> Union["Game", None]:
        """Performs a move on a copy of the puzzle state, and returns that new state.

        Keyword arguments:
        direction -- the direction to move the empty tile. Enumerated to up, down, left, right
        """
        result = tuple(sum(x) for x in zip(direction.value, self.empty_coord))  # type: ignore
        if not self.is_valid(result):
            return

        empty = (self.empty_coord[0], self.empty_coord[1])
        ret_state = deepcopy(self.state)

        (
            ret_state[empty[0]][empty[1]],
            ret_state[result[0]][result[1]],
        ) = (
            ret_state[result[0]][result[1]],
            ret_state[empty[0]][empty[1]],
        )
        # empty_coord = result
        return Game(ret_state, self.empty)

    def is_valid(self, coord: Tuple[int, ...]) -> bool:
        """Returns true if the input is a valid coordinate in the game board.

        Keyword arguments:
        coord -- the coordinate that is being checked
        """
        if (
            coord[0] < 0
            or coord[1] < 0
            or coord[0] >= self.height
            or coord[1] >= self.width
        ):
            return False

        return True

    def is_complete(self) -> bool:
        """Returns true if the puzzle has been solved."""
        return self.state == self.solution

    def manhattan_heuristic(self) -> int:
        """Returns the value given by the Manhattan distance of each character to
        its location in the solution.

        In the Angelica puzzle, there is exactly one instance of duplicates. As a result, we take the Manhattan distance such that the duplicate A's go to the closest solution coordinate.
        """
        # TODO: Implement heuristic
        ret = 0
        a_coords = []
        for row_idx, state_row in enumerate(self.state):
            for col_idx, state_cell in enumerate(state_row):
                if state_cell != "A":
                    sol_row, sol_col = self.solution_map[state_cell]
                    ret += abs(sol_row - row_idx) + abs(sol_col - col_idx)
                else:
                    a_coords.append((row_idx, col_idx))

        a_heur_1 = 0
        a_heur_2 = 0

        a_heur_1 += abs(a_coords[0][0]) + abs(a_coords[0][1])
        a_heur_1 += abs(a_coords[1][0] - 2) + abs(a_coords[1][1] - 1)

        a_heur_2 += abs(a_coords[1][0]) + abs(a_coords[1][1])
        a_heur_2 += abs(a_coords[0][0] - 2) + abs(a_coords[0][1] - 1)

        ret += min(a_heur_1, a_heur_2)

        return ret

    def misplaced_tile_heuristic(self) -> int:
        """Returns the number of characters that are not at the same coordinate as their solution counterpart."""

        ret = 0

        for sol_row, state_row in zip(self.solution, self.state):
            for sol_cell, state_cell in zip(sol_row, state_row):
                ret = ret if sol_cell == state_cell else ret + 1

        return ret


if __name__ == "__main__":
    game = Game()
    game = game.move(Move.LEFT)
    game = game.move(Move.UP)
    if game:
        print(game, end="\n\n")
        print(game.manhattan_heuristic())
