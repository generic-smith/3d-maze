# 0 = path
# 1 = wall
# 2 = entry point
# 3 = entrance to layer above
# 4 = entrance to layer below
# 5 = endpoint
examplemaze10by10by3 = [
    [
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 2, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 3, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]],

    [
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 4, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]],

    [
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
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


def solver(maze):
    start = find_start(maze)
    if not start:
        raise AttributeError("Beginning not found: \n" + display_path(maze))
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbors = get_neighbors(maze, node)
            for neighbor in neighbors:
                if neighbor not in explored:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if maze[neighbor[0]][neighbor[1]][neighbor[2]] == 5:
                        # print("shortest path found: {}".format(new_path))
                        return new_path
            explored.append(node)
    # print("no path found")
    return False


def get_neighbors(maze, node):
    valid_neighbors = []

    base = node
    # neighbor above
    if maze[base[0]][base[1]][base[2]] == 3:
        up = [base[0] + 1, base[1], base[2]]
        valid_neighbors.append(up)
    # neighbor below
    if maze[base[0]][base[1]][base[2]] == 4:
        down = [base[0] - 1, base[1], base[2]]
        valid_neighbors.append(down)

    # maximum index values to avoid quantum tunneling, wormholes, hyperspace or other scientific nonsense that allows
    # you to teleport like pac-man
    max_east = len(maze[0][0])
    max_south = len(maze[0])

    # getting coordinates of adjacent neighbors
    north = [base[0],
             0 if base[1] == 0 else base[1] - 1,
             base[2]]
    south = [base[0],
             max_south if base[1] == max_south else base[1] + 1,
             base[2]]
    west = [base[0],
            base[1],
            0 if base[2] == 0 else base[2] - 1]
    east = [base[0],
            base[1],
            max_east if base[2] == max_east else base[2] + 1]

    # making sure we don't walk face first into a wall
    for neighbor in [north, south, east, west]:
        try:
            val = maze[neighbor[0]][neighbor[1]][neighbor[2]]
            if val != 1:  # is neighbor not a wall?
                valid_neighbors.append(neighbor)
        except IndexError:
            neighbor = False
            # neighbor out of bounds of maze (somehow)

    return valid_neighbors


def find_start(maze):
    for z in range(len(maze)):
        for x in range(len(maze[z])):
            for y in range(len(maze[z][x])):
                if maze[z][x][y] == 2:
                    return [z, x, y]

    return False


def display_path(maze, path=False):
    new = maze
    toReturn = ""
    if not path:
        for layer in new:
            for row in layer:
                for x in row:
                    toReturn += str(x) + " "
                toReturn += '\n'
            toReturn += '\n'

    else:
        for node in path:
            new[node[0]][node[1]][node[2]] = 8 if new[node[0]][node[1]][node[2]] == 0 else new[node[0]][node[1]][
                node[2]]
        for layer in new:
            for row in layer:
                for x in row:
                    toReturn += str(x) + " "
                toReturn += '\n'
            toReturn += '\n'

    return toReturn
