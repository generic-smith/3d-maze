from random import random

from gen3dmaze import gen3dMaze
from maze_solver import solver, display_path

def errorTest(numTimes, verbose=False):
    errors = 0
    for x in range(numTimes):
        if verbose:
            print("round:", x)
        maze = gen3dMaze(int(random() * 5 + 5), int(random() * 5 + 5), int(random() * 4 + 1))
        # maze = gen3dMaze(int(4), int(5), int(3))

        try:
            solution = solver(maze)
        except AttributeError as e:
            print(e)
        if solution is False:
            errors += 1
            print("Maze: ")
            print(display_path(maze))
            print("---------------------------------------------------------------------------------")

    if verbose:
        print(errors, "errors found")
        if errors == 0:
            print("maze generation successful for", str(numTimes), "tests")
    return errors


errorTest(10000, verbose=True)


