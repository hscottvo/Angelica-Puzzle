from queue import PriorityQueue, Queue

from game import Game, Move


def uniform_cost_search(start: Game) -> None:
    search_queue = Queue()
    search_queue.put((0, start))

    while not search_queue.empty():
        num_moves, curr_game = search_queue.get()
        print(curr_game)
        print("")
        if curr_game.is_complete():
            print(f"Took {num_moves} moves to solve!")
            return
        for move in Move:
            new_game = curr_game.move(move)
            if new_game:
                search_queue.put((num_moves + 1, new_game))

    return


def misplaced_tile_search(start: Game) -> Game:
    return Game()


def manhattan_distance_search(start: Game) -> Game:
    return Game()


if __name__ == "__main__":
    game = Game()
    game = game.move(Move.LEFT)
    game = game.move(Move.LEFT)

    uniform_cost_search(game)
