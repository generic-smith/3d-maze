from gen3dmaze import gen3dMaze
from maze_solver import solver, display_path
from random import randrange
import time
from threading import Thread

errors = 0
runs = 10000
for i in range(runs):
    subtotal = 0
    print(i)

    start = time.time()
    # x = randrange(5, 10)
    # y = randrange(5, 10)
    # z = randrange(5, 10)
    z = 10
    x = 10
    y = 10
    print(x, y, z)

    try:
        maze = gen3dMaze(x, y, z)
        print("Created maze")
        print("Time: {}".format(time.time() - start))
        start = time.time()
        solution = solver(maze)
        print("Solved")
        solve_time = time.time() - start
        subtotal += solve_time
        print("Time: {}".format(solve_time))
    except AttributeError as e:
        print(e)
    if solution is False:
        errors += 1
        print("Maze: ")
        print(display_path(maze))
        print("---------------------------------------------------------------------------------")
print("avg solve time was: {}".format(subtotal / runs))
print(errors, "errors found")
