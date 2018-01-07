from copy import deepcopy


# a recursive function that generates all permutations of the elements of Alist
def permute(Alist, idx=0, Plist=None):
    if Plist == None:
        Plist = []
    """Logic inspired by http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
    """

    if idx >= len(Alist):
        Plist.append(Alist)

    for s in range(idx, len(Alist)):
        newList = deepcopy(Alist)
        newList[idx], newList[s] = newList[s], newList[idx]
        permute(newList, idx + 1, Plist)
    return Plist


# This flattens a singly nested list
def flatten(Alist):
    z = []
    for el in Alist:
        z.extend(el)
    return z


def makeBoxes(Alist, bRows, bCols):
    # Alist is list of lists of rows in nxn puzzle
    # brows, bcols are dimensions of inner box (e.g. 6x6 puzzle is made of 6 2x3 boxes, so makeBoxes(Alist,2,3)
    # This composes the inner boxes, numbering from top to bottom, left to right.
    # For example 6x6 = | box 0 | box 2 |
    #                   | box 1 | box 3 |

    puzzleSize = len(Alist)
    boxesAcrossCols = puzzleSize // bCols
    boxesDownRows = puzzleSize // bRows
    boxesTotal = boxesAcrossCols * boxesDownRows

    boxes = [[] for b in range(boxesTotal)]
    for b in range(boxesTotal):
        # Take all relevant column values from the bRows relevant to box "b"
        # For example, box 3 from above is composed of rows 2,3 and cols 2,3
        for row in range(b % boxesDownRows * bRows, b % boxesDownRows * bRows + bRows):
            boxes[b].extend(Alist[row][b // boxesDownRows * bCols: b // boxesDownRows * bCols + bCols])

    # print('\nBOXES')
    # for b in boxes: print(b)
    # print(boxes)
    return boxes


# make boxes function better suited for this problem
# Test makeBoxes
def testMakeBoxes():
    A = [[1, 2, 1, 2],
         [3, 1, 3, 2],
         [1, 2, 1, 2],
         [3, 3, 3, 4]]

    B2 = [
        [1, 2, 1, 2, 1, 2],
        [3, 4, 3, 4, 3, 4],
        [5, 6, 5, 6, 5, 6],
        [1, 2, 1, 2, 1, 2],
        [3, 4, 3, 4, 3, 4],
        [5, 6, 5, 6, 5, 6]]

    B = [[1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6],
         [1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6],
         [1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6]]

    C = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6, 4, 5, 6],
         [7, 8, 9, 7, 8, 9, 7, 8, 9],
         [1, 2, 3, 1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6, 4, 5, 6],
         [7, 8, 9, 7, 8, 9, 7, 8, 9],
         [1, 2, 3, 1, 2, 3, 1, 2, 3],
         [4, 5, 6, 4, 5, 6, 4, 5, 6],
         [7, 8, 9, 7, 8, 9, 7, 8, 9]]

    makeBoxes(A, 2, 2)
    # makeBoxes(B, 2, 3)
    # makeBoxes(B2, 3, 2)
    # makeBoxes(C, 3, 3)

# testMakeBoxes()
# print(permute([1, 2, 3]))
# print(permute([4, 5, 6]))
