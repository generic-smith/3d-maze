from random import random, randrange

# key:
# 0 = path
# 1 = wall
# 2 = entry point
# 3 = entrance to layer above
# 4 = entrance to layer below
# 5 = endpoint

examplemaze10by10by3 = [
    [[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 2, 1, 1, 1, 0, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 3, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]],

    [[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 4, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]],

    [[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 5, 1, 1, 1, 0, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 0, 4, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]],
]


class Point:
    def __eq__(self, o: object) -> bool:
        return isinstance(o, Point) and (self.x == o.x or self.y == o.y)

    def __init__(self, aX, aY, parent=None):
        self.x = aX
        self.y = aY
        self.parent = parent

    # compute opposite node given that it is in the other direction from the parent
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

    x = int(randrange(1 + (0 if xOdd else 1), width, 2))
    y = int(randrange(1 + (0 if yOdd else 1), height, 2))

    walls += [Point(x + 1, y, Point(x, y, None))]
    walls += [Point(x, y + 1, Point(x, y, None))]
    walls += [Point(x - 1, y, Point(x, y, None))]
    walls += [Point(x, y - 1, Point(x, y, None))]
    maze[x][y] = 0

    while len(walls) > 0:
        wallIndex = int(random() * len(walls))
        wallX = walls[wallIndex].x
        wallY = walls[wallIndex].y
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