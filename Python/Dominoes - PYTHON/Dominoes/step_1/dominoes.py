import random


class DominoSet:
    def __init__(self):
        self.tiles = self.generate_set()

    def generate_set(self) -> list:
        tiles = []
        for i in range(7):
            for j in range(7):
                tiles.append([i, j])
        random.shuffle(tiles)
        return tiles


class Tiles:
    def __init__(self):
        tiles = DominoSet().tiles
        self.stock_pieces = tiles[:14]
        self.player, self.computer = tiles[:7], tiles[7:14]
        self.snake, self.current_player = self.set_start()

    def set_start(self) -> (list, str):
        doubles_player = [tile for tile in self.player if tile[0] == tile[1]]
        doubles_computer = [tile for tile in self.computer if tile[0] == tile[1]]

        player_max = max(doubles_player, default=[-1, -1])
        computer_max = max(doubles_computer, default=[-1, -1])
        if player_max == computer_max:
            # This is an impossible condition unless both returned [-1,-1] above
            return None, None
        elif player_max > computer_max:
            self.player.remove(player_max)
            return [player_max], 'computer'
        else:
            self.computer.remove(computer_max)
            return [computer_max], 'player'

    def check_start(self) -> bool:
        return self.snake and self.current_player

    def reset(self):
        tiles = DominoSet().tiles
        self.stock_pieces = tiles[:14]
        self.player, self.computer = tiles[:7], tiles[7:14]
        self.snake, self.current_player = self.set_start()


class Dominos:
    def __init__(self):
        self.game = Tiles()

    def main(self):
        while not self.game.check_start():
            self.new_game()
        self.display_tiles()

    def display_tiles(self):
        print(f'Stock pieces: {self.game.stock_pieces}')
        print(f'Computer pieces: {self.game.computer}')
        print(f'Player pieces: {self.game.player}')
        print(f'Domino snake: {self.game.snake}')
        print(f'Status: {self.game.current_player}')

    def new_game(self):
        self.game.reset()


if __name__ == '__main__':
    game = Dominos()
    game.main()
