import numpy as np

direction_changes = {
    'e': [1, 0, -1],
    'w': [-1, 0, 1],
    'ne': [1, -1, 0],
    'nw': [0, -1, 1],
    'sw': [-1, 1, 0],
    'se': [0, 1, -1]
}


class TileSet:

    tiles = {}

    #False White
    #True Black

    @staticmethod
    def gen_key(pos):
        return str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2])

    @staticmethod
    def gen_coords(key):
        return list(map(int, key.split(",")))

    # counts black neighbors
    def count_neighbors(self, key):
        add_list = []
        black_neighbors = 0
        coords = TileSet.gen_coords(key)
        for change in direction_changes.values():
            neighbor_key = TileSet.gen_key(np.add(coords, change))
            if neighbor_key in self.tiles:
                if self.tiles[neighbor_key]:
                    black_neighbors +=1
            else:
                add_list.append(neighbor_key)
        return black_neighbors, add_list

    def get_color(self,key):
        if not(key in self.tiles):
            self.tiles[key] = False
        return self.tiles[key]


    def turn_tile(self, pos):
        key = TileSet.gen_key(pos)
        for change in direction_changes.values():
            neighbor_key = TileSet.gen_key(np.add(pos, change))
            if not(neighbor_key in self.tiles):
                self.tiles[neighbor_key] = False
        self.tiles[key] = not self.get_color(key)

    def count_black(self):
        count = 0
        for tile in self.tiles.values():
            if tile:
                count += 1
        return count

    def flip(self):
        flip_list = []
        add_list = []
        items = self.tiles.items()
        for key, value in items:
            neighbor_count, new_neighbor_list = self.count_neighbors(key)
            add_list.extend(new_neighbor_list)
            if value and ((neighbor_count > 2) or (neighbor_count == 0)):
                flip_list.append(key)
            if (not value) and (neighbor_count == 2):
                flip_list.append(key)
        for key in flip_list:
            self.tiles[key] = not self.tiles[key]
        for key in add_list:
            self.tiles[key] = False



def run():
    tiles = TileSet()
    with open("input.txt") as f:
        texts = f.readlines()
    for text in texts:
        text = text.strip()
        text_pos = 0
        tile_pos = [0,0,0]
        length = len(text)

        while text_pos < length:
            if text[text_pos] in ('e','w'):
                tile_pos = np.add(tile_pos, direction_changes[text[text_pos]])
                text_pos += 1
            else:
                tile_pos = np.add(tile_pos, direction_changes[text[text_pos:text_pos+2]])
                text_pos += 2
        tiles.turn_tile(tile_pos)
    print(tiles.count_black())
    for i in range(0,100):
        tiles.flip()
    print(tiles.count_black())


if __name__ == '__main__':
    run()