# This example is a simplistic "puzzle" in which the objective is to fill an nxn grid
# such that each row and each column contains exactly 1 instance of each of the numbers 1-n.
# It is a demonstration of how to code a puzzle solver using a generic BFS framework.

from copy import deepcopy
from functools import reduce

from helper import makeBoxes
from helper import flatten
from bfs import *
import execute


class Sudoku(object):
    def __init__(self, initial, size, r, c, goal=None):
        # These values are specific to the problem you are solving (i.e. sudoku, nQueens, ...)
        self.size = size
        self.initial = initial
        self.r = r
        self.c = c
        self.goal = goal

        # For this example, an action is the assignment of a single box
        # thus, the set of legal actions for all states is all numbers 1 to n
        self.actions = [i for i in range(1, self.size + 1)]

    def getActions(self, state):
        # All actions generated, regardless of being legal or illegal
        # print(self.actions)
        return self.actions

    def applyAction(self, state, action):

        # Creates newState with every call
        newState = deepcopy(state)

        # First flatten the state to determine the row and column in which to place the number
        flat = flatten(state)
        # Store location of where the first empty box (0) is in the flattened state
        zero = flat.index(0)

        # Translates zero location into row-column coordinates
        row = zero // self.size
        col = zero % self.size
        # print(action)
        # print(row,col)
        # Create seperate lists for the individual rows and columns in the state
        entire_row = newState[row]
        column = flat[col::(col + self.size)]

        # Boolean variables initialized to False. If they are true then that type of pruning will occur
        prune_rc = False
        prune_box = False

        # PRUNING BEGINS HERE
        #
        if action in entire_row or action in column:
            prune_rc = True
            # pass # Does not add action to tree if any of above pruning criteria are true
        # Creates boxes with custom box making function
        # Marks row to find with -1
        temp = newState[row][col]
        newState[row][col] = -1
        box = makeBoxes(newState, self.r, self.c)
        for rows in box:
            if -1 in rows:
                if action in rows:
                    prune_box = True
        newState[row][col] = temp

        if prune_rc or prune_box:
            return []
            # Creates a new state by applying a legal action. Numbers that have already been given
            # are never changed
        else:
            newState[row][col] = action
            # print(newState)
            return newState

    def isGoal(self, state):
        # Again, problem specific code.

        # If the state is empty, not done yet
        if not state:
            return False

        # If any box has a zero, not done yet
        for x in range(len(state)):
            for y in range(len(state[x])):
                # print(state)
                if state[x][y] == 0:
                    return False

        # We have a completely filled in board. Check if there are any
        # duplicates across columns or rows
        for row in state:
            if len(list(set(row))) < self.size:
                return False
        for col in range(self.size):
            if len(list(set([row[col] for row in state]))) < self.size:
                # print('State ',state,' not goal')
                return False

        # If we got here, the board is complete and legal
        print('WINNER')
        for i in range(self.size):
            output = ''
            for j in range(self.size):
                output += '   ' + str(state[i][j])
            print(output)
        return True


p1 = [[1, 0, 3, 0],
      [0, 3, 0, 0],
      [0, 2, 0, 0],
      [4, 0, 0, 0]]

p2 = [[0, 0, 0, 0, 4, 0],
      [5, 6, 0, 0, 0, 0],

      [3, 0, 2, 6, 5, 4],
      [0, 4, 0, 2, 0, 3],

      [4, 0, 0, 0, 6, 5],
      [1, 5, 6, 0, 0, 0]]
p3 = [[0, 0, 0, 8, 4, 0, 6, 5, 0],
      [0, 8, 0, 0, 0, 0, 0, 0, 9],
      [0, 0, 0, 0, 0, 5, 2, 0, 1],

      [0, 3, 4, 0, 7, 0, 5, 0, 6],
      [0, 6, 0, 2, 5, 1, 0, 3, 0],
      [5, 0, 9, 0, 6, 0, 7, 2, 0],

      [1, 0, 8, 5, 0, 0, 0, 0, 0],
      [6, 0, 0, 0, 0, 0, 0, 4, 0],
      [0, 5, 2, 0, 8, 6, 0, 0, 0]]
BFS(Sudoku(p1, len(p1),2,2))
BFS(Sudoku(p1, len(p1),2,2))
DFS(Sudoku(p1, len(p1),2,2))
DFS(Sudoku(p3,len(p3),3,3))
