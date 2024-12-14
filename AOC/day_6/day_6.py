import json


class GuardGallivant:
    def __init__(self):
        with open("day_6.txt", 'r') as f:
            self.grid = [list(line.strip()) for line in f]

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "^":
                    self.start = (i, j)
                    break

    def moves(self, position, state):
        x, y = state
        positions = {
            "^": (x - 1, y),
            "v": (x + 1, y),
            "<": (x, y - 1),
            ">": (x, y + 1),
        }
        return positions[position]

    def neighbors(self):
        state = self.start
        start_position = "^"
        explored = set()

        while True:
            x, y = self.moves(start_position, state)

            if 0 <= x < self.height and 0 <= y < self.width:
                if self.grid[x][y] == "#":
                    if start_position == "^":
                        start_position = ">"
                    elif start_position == ">":
                        start_position = "v"
                    elif start_position == "v":
                        start_position = "<"
                    elif start_position == "<":
                        start_position = "^"
                else:
                    explored.add((x, y))
                    state = (x, y)
            else:

                explored.add((x, y))
                return len(explored), explored

    def part2(self):
        old_v, visited_positions = self.neighbors()
        c = 0

        for x, y in visited_positions:
            self.grid[x][y] = "#"


            v, _ = self.neighbors()

            if v < old_v:
                c += 1

            self.grid[x][y] = "."
        return c


if __name__ == "__main__":
    gg = GuardGallivant()
    print(gg.part2())
