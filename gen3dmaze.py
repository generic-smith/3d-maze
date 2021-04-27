from random import randrange
from prim2dmaze import gen2dmaze as genMaze

# key:
# 0 = path
# 1 = wall
# 2 = entry/start point
# 3 = entrance to layer above
# 4 = entrance to layer below
# 5 = endpoint

def gen3dMaze(width, height, depth, verbose=False):
    maze = []

    for z in range(depth):  # build the layers of the maze
        maze.append(genMaze(width, height))
        if verbose:
            print("Built layer:", z)
    # add the ladders and slides between layers
    slide = None

    y = randrange(0, height, 1)  # pick random x for first floor ladder
    x = randrange(0, width, 1)  # pick random y for first floor ladder
    while maze[0][x][y] != 0:  # repeat until the slide being created a valid maze point
        x = randrange(0, width, 1)
        y = randrange(0, height, 1)

    ladder = [x, y]

    for z in range(len(maze)):  # open up all of the chutes and ladders
        if slide is not None:  # if this is not the first layer
            maze[z][slide[0]][slide[1]] = 4
        if z != depth - 1:  # if this is not the top layer
            maze[z][ladder[0]][ladder[1]] = 3

        slide = ladder

        y = randrange(0, height, 1)
        x = randrange(0, width, 1)
        while maze[z][x][y] != 0:  # select a valid spot to add the next ladder
            x = randrange(0, width, 1)
            y = randrange(0, height, 1)

        ladder = [x, y]

    for num in [2, 5]:  # add in the start and endpoints of the maze
        x = randrange(0, width, 1)
        y = randrange(0, height, 1)
        z = randrange(0, depth, 1)
        while maze[z][x][y] != 0:
            x = randrange(0, width, 1)
            y = randrange(0, height, 1)
            z = randrange(0, depth, 1)

        maze[z][x][y] = num

    return maze
