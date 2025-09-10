import sys

class Node():
    def __init__(self, state, parent, action, time, cheats_used):
        self.state = state
        self.parent = parent
        self.action = action
        self.time = time  # Time corresponds to the number of steps
        self.cheats_used = cheats_used  # Number of cheats used

class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop(0)  # FIFO, remove from the front
            return node

class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("S") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("E") != 1:
            raise Exception("maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "S":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "E":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == ".":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.cheats = []

    def neighbors(self, state, cheats_used):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width:
                if not self.walls[r][c]:  # Open path
                    result.append((action, (r, c), cheats_used))
                elif cheats_used < 2:  # Wall but cheats available
                    result.append((action, (r, c), cheats_used + 1))
        return result

    def solve_with_cheats(self):
        self.num_explored = 0
        start = Node(state=self.start, parent=None, action=None, time=0, cheats_used=0)
        frontier = QueueFrontier()
        frontier.add(start)  # Add the start node to the frontier

        self.explored = set()
        baseline_time = None

        while True:
            if frontier.empty():
                break

            node = frontier.remove()
            self.num_explored += 1

            # Debug: Print the current node and time
            print(f"Exploring node at {node.state} with {node.cheats_used} cheats, Time = {node.time}")

            # When we reach the goal, we can compute the baseline time
            if node.state == self.goal:
                if baseline_time is None:
                    baseline_time = node.time  # Set baseline time
                    print(f"First solution time (without cheats): {baseline_time}")
                else:
                    time_saved = baseline_time - node.time
                    print(f"Goal reached with {node.cheats_used} cheats: Time = {node.time}, Time saved = {time_saved}")

                # Track the time saved by using cheats
                if time_saved > 0:
                    self.cheats.append(time_saved)
                continue

            self.explored.add((node.state, node.cheats_used))  # Avoid re-exploring the same state with the same number of cheats

            # Debug: Show possible neighbors
            neighbors = self.neighbors(node.state, node.cheats_used)
            for action, state, new_cheats_used in neighbors:
                print(f"  Neighbor: {action} -> {state}, Cheats used: {new_cheats_used}")

            # Explore neighbors, taking cheats into account
            for action, state, new_cheats_used in neighbors:
                if (state, new_cheats_used) not in self.explored:
                    child = Node(state=state, parent=node, action=action, time=node.time + 1, cheats_used=new_cheats_used)
                    frontier.add(child)

    def count_cheats(self, threshold):
        return len([cheat for cheat in self.cheats if cheat >= threshold])

if len(sys.argv) != 2:
    sys.exit("Usage: python AOC20.py dataaoc20test.txt")

m = Maze(sys.argv[1])
m.solve_with_cheats()

threshold = 100
count = m.count_cheats(threshold)
print(f"Number of cheats saving at least {threshold} picoseconds: {count}")
