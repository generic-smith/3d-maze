from random import randrange

from prim2dmaze import gen2dmaze as genMaze


# key:
# 0 = path
# 1 = wall
# 2 = entry point
# 3 = entrance to layer above
# 4 = entrance to layer below
# 5 = endpoint

def gen3dMaze(width, height, depth):
    maze = []

    for z in range(depth):  # build the layers of the maze
        maze.append(genMaze(width, height))
        print("Built layer:", z)
    # add the ladders and slides between layers
    slide = None

    y = randrange(0, height, 1)
    x = randrange(0, width, 1)
    while maze[0][x][y] != 0:
        x = randrange(0, width, 1)
        y = randrange(0, height, 1)

    ladder = [x, y]

    for z in range(len(maze)):
        if slide is not None:
            maze[z][slide[0]][slide[1]] = 4
        if z != depth - 1:
            maze[z][ladder[0]][ladder[1]] = 3

        slide = ladder

        y = randrange(0, height, 1)
        x = randrange(0, width, 1)
        while maze[z][x][y] != 0:
            x = randrange(0, width, 1)
            y = randrange(0, height, 1)

        ladder = [x, y]

    for num in [2, 5]:
        x = randrange(0, width, 1)
        y = randrange(0, height, 1)
        z = randrange(0, depth, 1)
        while maze[z][x][y] != 0:
            x = randrange(0, width, 1)
            y = randrange(0, height, 1)
            z = randrange(0, depth, 1)

        maze[z][x][y] = num

    return maze


"""maze = gen3dMaze(6, 6, 5)

for x in maze:
    for y in x:
        print(y)
    print()"""
