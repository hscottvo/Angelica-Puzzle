from queue import PriorityQueue

from game import Game, Move


def search(start: Game, verbose: bool = True) -> Game:
    num_nodes = 0
    max_queue_size = 0
    search_queue = PriorityQueue()
    search_queue.put(start)
    visited = set()

    while not search_queue.empty():
        curr_game = search_queue.get()

        if curr_game.flatten() in visited:
            continue
        else:
            visited.add(curr_game.flatten())

        if verbose:
            num_nodes += 1
            g = curr_game.get_num_moves()
            h = curr_game.heuristic() - curr_game.get_num_moves()
            print(f"The best state to expand with g(n) = {g} and h(n) = {h} is:")
            print(curr_game, end="\n\n")

        if curr_game.is_complete():
            num_moves = curr_game.get_num_moves()
            print(f"Finished in {num_moves} moves!")
            if verbose:
                print(f"Expanded {num_nodes} nodes")
                print(f"Longest queue size: {max_queue_size} nodes")
                print("History:")
                print(curr_game.get_history())
            return curr_game
        for move in Move:
            next_game = curr_game.move(move)
            if next_game is None:
                continue

            if verbose:
                max_queue_size = max(max_queue_size, search_queue.qsize())

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
        game.reset()
        game = search(game)
