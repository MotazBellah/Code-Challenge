class SearchXMAS:
    def __init__(self):
        with open("day_4.txt", 'r') as f:
            self.grid = [list(line.strip()) for line in f]

        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.word_to_find = "XMAS"

    def neighbors(self, state):
        x, y = state
        candidates = [
            ("left", [(x, y - i) for i in range(1, len(self.word_to_find))]),
            ("right", [(x, y + i) for i in range(1, len(self.word_to_find))]),
            ("up", [(x - i, y) for i in range(1, len(self.word_to_find))]),
            ("down", [(x + i, y) for i in range(1, len(self.word_to_find))]),
            ("diagonal1", [(x + i, y + i) for i in range(1, len(self.word_to_find))]),
            ("diagonal2", [(x - i, y - i) for i in range(1, len(self.word_to_find))]),
            ("anti-diagonal1", [(x - i, y + i) for i in range(1, len(self.word_to_find))]),
            ("anti-diagonal2", [(x + i, y - i) for i in range(1, len(self.word_to_find))]),
        ]

        result = []
        for action, path in candidates:
            valid_path = [(x, y)]
            for r, c in path:
                if 0 <= r < self.height and 0 <= c < self.width:
                    valid_path.append((r, c))

            if len(valid_path) == len(self.word_to_find):
                result.append((action, valid_path))
        return result

    def dfs_search(self):
        c = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == self.word_to_find[0]:
                    start = (x, y)
                    for action, path in self.neighbors(start):
                        word = "".join(self.grid[r][c] for r, c in path)
                        if word == self.word_to_find:
                            c += 1
        return c

class SearchXShape(SearchXMAS):
    def __init__(self):
        super().__init__()

    def x_search(self):
        c = 0

        for x in range(self.height - 1):
            for y in range(self.width - 1):
                if self.grid[x][y] == "A":
                    top_left = self.grid[x - 1][y - 1]
                    bottom_right = self.grid[x + 1][y + 1]
                    top_right = self.grid[x - 1][y + 1]
                    bottom_left = self.grid[x + 1][y - 1]

                    if (
                        (top_left == "M" and bottom_right == "S" or top_left == "S" and bottom_right == "M") and
                        (top_right == "M" and bottom_left == "S" or top_right == "S" and bottom_left == "M")
                    ):
                        c += 1

        return c



if __name__ == "__main__":
    xmas = SearchXMAS()
    part1 = xmas.dfs_search()
    x_shape = SearchXShape()
    part2 = x_shape.x_search()
    print(part2)