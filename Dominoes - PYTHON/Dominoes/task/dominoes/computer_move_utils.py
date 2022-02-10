class ComputerMoveUtils:

    @staticmethod
    def count_occurrences(tiles: list) -> dict:
        """Iterate through each tile in the tile list and count the occurrences of each number"""
        counts = {}
        for tile in tiles:
            if tile[0] in counts:
                counts[tile[0]] += 1
            else:
                counts[tile[0]] = 1
            if tile[1] in counts:
                counts[tile[1]] += 1
            else:
                counts[tile[1]] = 1
        return counts

    @staticmethod
    def generate_sorted_point_list(counts: dict, tiles: list) -> list:
        points_list = []
        for tile in tiles:
            elem_list = [tile, counts.get(tile[0]) + counts.get(tile[1])]
            points_list.append(elem_list)

        points_list.sort(key=lambda elem: elem[1], reverse=True)
        return points_list

    @staticmethod
    def determine_move_side_and_target(tiles: list, points_list: list) -> (int, int):
        """Return the side and target number for the optimal solution, or 0/None if none exists."""
        for tile_point in points_list:
            if tiles[0][0] in (tile_point[0][0], tile_point[0][1]):
                return -1, tile_point[0]
            elif tiles[-1][1] in (tile_point[0][1], tile_point[0][1]):
                return 1, tile_point[0]
        return 0, None
