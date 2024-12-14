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
        seen_states = set()

        while True:
            x, y = self.moves(start_position, state)

            if (state, start_position) in seen_states:
                return len(explored), explored, True

            seen_states.add((state, start_position))
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
                return len(explored), explored, False

    def part2(self):
        _, visited_positions, _ = self.neighbors()
        c = 0

        for x, y in visited_positions:
            if not (0 <= x < self.height and 0 <= y < self.width):
                continue

            self.grid[x][y] = "#"
            _, _, seen = self.neighbors()

            if seen:
                c += 1

            self.grid[x][y] = "."
        return c


if __name__ == "__main__":
    gg = GuardGallivant()
    print(gg.part2())
