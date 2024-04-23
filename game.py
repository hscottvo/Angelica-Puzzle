from enum import Enum
from typing import List


class Move(Enum):
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    UP = (-1, 0)


class Game:
    start_state = [["A", "N", "G"], ["E", "L", "I"], ["C", "A", "\u25a1"]]

    def __init__(self, state: List[List[str]] = start_state, empty: str = "\u25a1"):
        self.state = state
        self.empty = empty
        self.height = len(state)
        assert self.height > 0
        self.width = len(state[0])
        self.__check_size()
        self.__assign_empty()

    def __check_size(self):
        for i in self.state:
            if len(i) != self.width:
                raise Exception("Width must be greater than 0!")

    def __assign_empty(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                if self.state[i][j] == self.empty:
                    self.empty_coord = (i, j)

    def __str__(self) -> str:
        return "\n".join([" ".join([i for i in row]) for row in self.state])

    def move(self, direction: Move) -> None:
        print(direction.value)
        result = tuple(sum(x) for x in zip(direction.value, self.empty_coord))
        print(
            f"Current empty: {self.empty_coord}, move: {direction.value}, end: {result}"
        )
        return


if __name__ == "__main__":
    game = Game()
    print(game)
    game.move(Move.DOWN)
