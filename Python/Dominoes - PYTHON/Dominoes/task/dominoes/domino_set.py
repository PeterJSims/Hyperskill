import random


class DominoSet:
    def __init__(self):
        self.tiles = DominoSet.generate_set()

    @staticmethod
    def generate_set() -> list:
        """Generate a set of tiles ranging from [0,0] to [6, 6]"""
        tiles = []
        for i in range(7):
            for j in range(i, 7):
                tiles.append([i, j])
        random.shuffle(tiles)
        return tiles
