from random import random, randrange


# key:
# 0 = path
# 1 = wall
# 2 = entry point
# 3 = entrance to layer above
# 4 = entrance to layer below
# 5 = endpoint

'''
    Mazes are represented using the Key above. Essential the maze is
    designed such that every even pair of coordinates in the maze represents
    a node. Every other pair of coordinates represents an edge connecting the 
    nodes. The algorithm works by randomly selecting a starting node and then
    expanding out from that node. Each as new nodes are added as paths in the 
    maze, the surrounding walls of the node are added to the list of edges. 
    Each round, an edge is randomly selected from that list. If turning that 
    edge wall into a path would not result in a loop (i.e. it is not neighboring
    more than 1 path square) that the edge and corresponding vertices are 
    all made into path squares. This is repeated until there are no remaining 
    edges/walls remaining in the list of neighboring walls/edges.
'''

class Point:  # this represents a single edge or node in the array. The parent of the
              # Point is the preceding point which this point is connecting to.

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Point) and (self.x == o.x or self.y == o.y)

    def __init__(self, aX, aY, parent=None):
        self.x = aX
        self.y = aY
        self.parent = parent

    # compute the coordinates of the node on the opposite side of this points from the parent
    def opposite(self):
        if self.x - self.parent.x != 0:
            return Point(self.x + (self.x - self.parent.x), self.y, self)
        if self.y - self.parent.y != 0:
            return Point(self.x, self.y + (self.y - self.parent.y), self)
        return None

    def __str__(self):
        return "[" + self.x + ", " + self.y + "]"


def gen2dmaze(width, height, xOdd=False, yOdd=False):
    maze = []  # initialize maze to desired specifications

    for x in range(width):
        maze.append([])
        for y in range(height):
            maze[x].append(1)

    walls = []

    x = int(randrange(1 + (0 if xOdd else 1), width, 2))  # randomly generate a number to
                                                          # be the initial x coordinate
    y = int(randrange(1 + (0 if yOdd else 1), height, 2)) # randomly generate a number to
                                                          # be the initial y coordinate

    # add all of the walls neighboring the initial point into the walls list
    walls += [Point(x + 1, y, Point(x, y, None))]
    walls += [Point(x, y + 1, Point(x, y, None))]
    walls += [Point(x - 1, y, Point(x, y, None))]
    walls += [Point(x, y - 1, Point(x, y, None))]

    maze[x][y] = 0  # make the initial point a path

    while len(walls) > 0:  # iterate until there are no more available edges
        wallIndex = int(random() * len(walls))  # select a random edge from the list of viable edges
        wallX = walls[wallIndex].x  # get the x coordinate of the wall
        wallY = walls[wallIndex].y  # get the y coordinate of the wall
        opposite = walls[wallIndex].opposite()
        walls.pop(wallIndex)

        try:
            # check if opposite and current are both walls
            if maze[wallX][wallY] + maze[opposite.x][opposite.y] == 2:
                if wallX < 0 or wallY < 0 or opposite.x < 0 or opposite.y < 0:
                    raise IndexError
                # if so, open path between them
                maze[wallX][wallY] = 0
                maze[opposite.x][opposite.y] = 0

                # add surrounding walls to the walls array
                if maze[opposite.x - 1][opposite.y] != 0:
                    if opposite.x - 1 < 0:
                        raise IndexError
                    walls += [Point(opposite.x - 1, opposite.y, opposite)]
                if maze[opposite.x][opposite.y - 1] != 0:
                    if opposite.x - 1 < 0:
                        raise IndexError
                    walls += [Point(opposite.x, opposite.y - 1, opposite)]
                if maze[opposite.x + 1][opposite.y] != 0:
                    walls += [Point(opposite.x + 1, opposite.y, opposite)]
                if maze[opposite.x][opposite.y + 1] != 0:
                    walls += [Point(opposite.x, opposite.y + 1, opposite)]
        except IndexError:
            pass

    """toReturn = []

    yAdd = 1 if yOdd else 0
    xAdd = 0 if xOdd else 1

    for x in maze[yAdd: width + yAdd]:
        toReturn.append(x[xAdd: height + xAdd])
    return toReturn"""

    return maze
