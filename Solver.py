from bfs import *
from Sudoku import *


def Solver(puzzle, r, c, search="bfs", printSolution=False):
    if search == "bfs":
        call = BFS(Sudoku(puzzle, len(puzzle), r, c))

    elif search == "dfs":
        call = DFS(Sudoku(puzzle, len(puzzle), r, c))
    else:
        call = "Invalid search"
    if printSolution:
        if call == None:
            print("No Solution")
        return call
    else:
        return call


p1 = [[1, 0, 3, 0],
      [0, 3, 0, 0],
      [0, 2, 0, 0],
      [4, 0, 0, 0]]
# Solver(p1, 2,2,"bfs",True)
