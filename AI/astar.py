import heapq

class Board:
    def __init__(self, queens):
        self.queens = queens  # queens[i] = column of queen in row i

    def is_goal(self):
        return len(self.queens) == 8 and self.heuristic() == 0

    def heuristic(self):
        # Number of pairs of queens attacking each other
        h = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j] or \
                   abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    h += 1
        return h

    def get_successors(self):
        successors = []
        row = len(self.queens)
        for col in range(8):
            if col not in self.queens:  # optional pruning
                new_board = Board(self.queens + [col])
                successors.append(new_board)
        return successors

    def __lt__(self, other):
        return True  # arbitrary tie-breaker for heapq

    def __str__(self):
        board = ""
        for row in range(8):
            line = ""
            for col in range(8):
                line += "Q " if row < len(self.queens) and self.queens[row] == col else ". "
            board += line.strip() + "\n"
        return board.strip()

def a_star_8_queens():
    start = Board([])
    open_list = []
    heapq.heappush(open_list, (start.heuristic(), 0, start))

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current.is_goal():
            print("Solution Found:\n")
            print(current)
            return current

        for neighbor in current.get_successors():
            heapq.heappush(open_list, (g + 1 + neighbor.heuristic(), g + 1, neighbor))

    print("No solution found.")
    return None

# Run the A* 8-Queens solver
a_star_8_queens()
