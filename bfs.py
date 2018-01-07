# The intent with these search functions is to create a generic framework that can
# be applied to any problem. It should be configured so that you can use both this search and the
# Node class without modification, provided you write problem specific code in the Problem class

from copy import deepcopy
from collections import deque


class Node:
    nodeCount = 0

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.nodeCount = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        # print('actions:',problem.getActions(self.state))
        a = [self.makeChild(problem, action) for action in problem.getActions(self.state)]
        # print(a)
        return a

    def makeChild(self, problem, action):
        Node.nodeCount += 1
        # if 0 == (Node.nodeCount % 100) :
        #	print( 'nodeCount: ',Node.nodeCount )
        childState = problem.applyAction(self.state, action)
        if not childState:
            return []
        return Node(childState)

    def getState(self):
        return self.state


def BFS(problem):
    # Generate the initial (root) node
    node = Node(problem.initial)

    # For efficiency, we check if the node is a goal state BEFORE putting on the Q
    if problem.isGoal(node.getState()):
        return node

    # Start the frontier Q by adding the root
    frontier = deque()
    frontier.append(node)

    # Test functions below for understanding
    # print(node.getState())

    # Keep searching the tree until there is nothing left to explore (i.e. frontier is empty)
    # OR a solution is found
    while len(frontier) > 0:
        node = frontier.popleft()
        # POTENTIAL IMPROVEMENT: Use a generator to feed the loop 1 element at a time
        for child in node.expand(problem):
            if child:
                if problem.isGoal(child.getState()):
                    return child
                frontier.append(child)
    return None


def DFS(problem):
    # Generate the initial (root) node
    node = Node(problem.initial)

    # For efficiency, we check if the node is a goal state BEFORE putting on the Q
    if problem.isGoal(node.getState()):
        return node

    # Start the frontier Q by adding the root
    frontier = deque()
    frontier.append(node)

    # Test functions below for understanding
    # print(node.getState())

    # Keep searching the tree until there is nothing left to explore (i.e. frontier is empty)
    # OR a solution is found
    while len(frontier) > 0:
        node = frontier.pop()
        # POTENTIAL IMPROVEMENT: Use a generator to feed the loop 1 element at a time
        for child in node.expand(problem):
            if child:
                if problem.isGoal(child.getState()):
                    return child
                frontier.append(child)
    return None
