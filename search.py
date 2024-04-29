from queue import PriorityQueue

from game import Game, Move


def search(start: Game) -> Game:
    search_queue = PriorityQueue()
    search_queue.put(start)
    visited = set()

    while not search_queue.empty():
        curr_game = search_queue.get()
        if curr_game.flatten() in visited:
            continue
        else:
            visited.add(curr_game.flatten())
        if curr_game.is_complete():
            num_moves = curr_game.get_num_moves()
            print(f"Finished in {num_moves} moves!")
            return curr_game
        for move in Move:
            next_game = curr_game.move(move)
            if next_game is None:
                continue
            search_queue.put(next_game)
    print("Unsolveable!")
    return Game()


if __name__ == "__main__":
    game = Game(heuristic="manhattan")
    # game.state[0][0], game.state[0][1] = game.state[0][1], game.state[0][0]
    game = game.move(Move.UP)
    if game:
        game = game.move(Move.LEFT)
    if game:
        game = game.move(Move.UP)
    if game:
        game.reset_num_moves()
        game = search(game)
