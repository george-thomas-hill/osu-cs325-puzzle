# This Python code was based on the BFS pseudo-code found at:
# https://brilliant.org/wiki/breadth-first-search-bfs/

from collections import deque


def solve_puzzle(Board, Source, Destination):

    def getNextCoordinates(current, direction):
        oldRow, oldColumn = current

        newRow = oldRow
        newColumn = oldColumn

        legal = True

        if direction == "U":
            newRow = oldRow - 1
        elif direction == "D":
            newRow = oldRow + 1
        elif direction == "L":
            newColumn = oldColumn - 1
        else:
            newColumn = oldColumn + 1

        if newRow < 1 or newRow > len(Board):
            legal = False
        if newColumn < 1 or newColumn > len(Board[0]):
            legal = False

        if legal == True:
            if Board[newRow - 1][newColumn - 1] == "#":
                legal = False

        return legal, (newRow, newColumn)

    queue = deque()
    queue.append((Source, 0, ""))
    visited = {}
    visited[Source] = True

    while(queue):
        current, step, path = queue.popleft()
        for direction in ["L", "R", "U", "D"]:
            legal, nextStop = getNextCoordinates(current, direction)
            if not legal:
                continue
            elif nextStop in visited:
                continue
            elif nextStop == Destination:
                return (step + 1 - 1, path + direction)
            else:
                visited[nextStop] = True
                queue.append((nextStop, step + 1, path + direction))
    return None


# Test cases follow.

board = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["#", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-"]
]

print(solve_puzzle(board, (1, 3), (3, 3))) # (3, 'LDDR')

print(solve_puzzle(board, (1, 1), (5, 5))) # (7, 'RRRRDDDD')

print(solve_puzzle(board, (1, 1), (5, 1))) # None

board = [
    ["-", "-", "-", "-", "#"],
    ["-", "-", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["#", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-"]
]

print(solve_puzzle(board, (1, 1), (5, 5))) # (7, 'RRRDRDDD')
