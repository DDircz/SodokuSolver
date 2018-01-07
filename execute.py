# from uniqueFillv1 import *
# from uniqueFillv2 import *
#
#
# def runv1(n=3, test=''):
#     if ('test' == test):
#         testv1()
#     else:
#         BFS(UF1problem([], n))
#
#
# def runv2(n=3, test=''):
#     if ('test' == test):
#         testv2()
#     else:
#         BFS(UF2problem([], n))
#
#
# def runv2DFS(n=3, test=''):
#     if ('test' == test):
#         testv2()
#     else:
#         DFS(UF2problem([], n))


# runv1(3,'test')
# runv1(3)
# runv1(4)

# runv2(3,'test')
# runv2(3)
# runv2(4)   # This will run for hours in its given form. Pruning would be essential to make this work!
# runv2DFS(3)

# Here are the sample Sudoku to use for testing
p1 = [[1, 5, 0, 0, 4, 0],
      [2, 4, 0, 0, 5, 6],

      [4, 0, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 4],

      [6, 3, 0, 0, 2, 0],
      [0, 2, 0, 0, 3, 1]]

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

# BFS(UF2problem(p1, 6))
