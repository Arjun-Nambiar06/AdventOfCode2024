import sys
from heapq import heappop, heappush

class Node:
    def __init__(self, state, parent, action, direction, cost):
        self.state = state  # (row, col)
        self.parent = parent
        self.action = action  # "up", "down", "left", "right"
        self.direction = direction  # "N", "S", "E", "W"
        self.cost = cost  # cumulative score

    def __lt__(self, other):
        return self.cost < other.cost  # Priority based on cost

class Maze:
    DIRECTIONS = {
        "N": (-1, 0),  # up
        "S": (1, 0),   # down
        "E": (0, 1),   # right
        "W": (0, -1)   # left
    }
    TURN_COST = 1000
    MOVE_COST = 1

    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("S") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("E") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls and positions
        self.walls = []
        for i, line in enumerate(contents):
            row = []
            for j, char in enumerate(line):
                if char == "S":
                    self.start = (i, j)
                    row.append(False)
                elif char == "E":
                    self.goal = (i, j)
                    row.append(False)
                elif char == "#":
                    row.append(True)
                else:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("S", end="")
                elif (i, j) == self.goal:
                    print("E", end="")
                elif solution and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state, direction):
        row, col = state
        for d, (dr, dc) in self.DIRECTIONS.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.height and 0 <= new_col < self.width and not self.walls[new_row][new_col]:
                turn_cost = self.TURN_COST if direction != d else 0
                yield (d, (new_row, new_col), turn_cost)  # Yield direction change cost

    def solve(self):
        # Priority queue (min-heap)
        frontier = []
        heappush(frontier, Node(self.start, None, None, "E", 0))  # Start facing East

        # Explored states with their lowest cost
        explored = {}

        while frontier:
            node = heappop(frontier)

            # If goal is reached, reconstruct the path
            if node.state == self.goal:
                actions, cells = [], []
                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                print(f"Minimal score: {node.cost}")  # Print the minimal score
                return

            # Skip if this state has been visited with a lower cost
            if node.state in explored and explored[node.state] <= node.cost:
                continue

            explored[node.state] = node.cost

            # Add neighbors to the frontier
            for action, new_state, turn_cost in self.neighbors(node.state, node.direction):
                new_cost = node.cost + self.MOVE_COST + turn_cost
                print(f"Exploring: {new_state} with cost: {new_cost} (turn cost: {turn_cost})")  # Debug print
                heappush(frontier, Node(new_state, node, action, action, new_cost))

        raise Exception("No solution found")

# Load the maze and solve it
if len(sys.argv) != 2:
    print("Usage: python reindeer_maze.py maze.txt")
    sys.exit(1)

maze = Maze(sys.argv[1])
maze.solve()
maze.print()
