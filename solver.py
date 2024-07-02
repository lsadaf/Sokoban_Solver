import queue
import copy


def updateMaze(maze, move, i, j):
    x, y = i, j
    if move == "r":
        if maze[x][y] == "ba":
            maze[x][y] = "b"
        else:
            maze[x][y] = "f"
        if y + 2 <= len(maze[0]) and maze[x][y + 1] == "s":
            maze[x][y + 1] = "f"
            if maze[x][y + 2] == 'b':
                maze[x][y + 2] = 'bs'
            else:
                maze[x][y + 2] = 's'
        if maze[x][y + 1] == 'b':
            maze[x][y + 1] = "ba"
        else:
            maze[x][y + 1] = "a"
    elif move == "l":
        if maze[x][y] == "ba":
            maze[x][y] = "b"
        else:
            maze[x][y] = "f"
        if y - 2 >= 0 and maze[x][y - 1] == "s":
            maze[x][y - 1] = "f"
            if maze[x][y - 2] == 'b':
                maze[x][y - 2] = 'bs'
            else:
                maze[x][y - 2] = 's'
        if maze[x][y - 1] == 'b':
            maze[x][y - 1] = "ba"
        else:
            maze[x][y - 1] = "a"
    elif move == "u":
        if maze[x][y] == "ba":
            maze[x][y] = "b"
        else:
            maze[x][y] = "f"
        if x - 2 >= 0 and maze[x - 1][y] == "s":
            maze[x - 1][y] = "f"
            if maze[x - 2][y] == 'b':
                maze[x - 2][y] = 'bs'
            else:
                maze[x - 2][y] = 's'
        if maze[x - 1][y] == 'b':
            maze[x - 1][y] = "ba"
        else:
            maze[x - 1][y] = "a"
    elif move == "d":
        if maze[x][y] == "ba":
            maze[x][y] = "b"
        else:
            maze[x][y] = "f"
        if x + 2 <= len(maze) and maze[x + 1][y] == "s":
            maze[x + 1][y] = "f"
            if maze[x + 2][y] == 'b':
                maze[x + 2][y] = 'bs'
            else:
                maze[x + 2][y] = 's'
        if maze[x + 1][y] == 'b':
            maze[x + 1][y] = "ba"
        else:
            maze[x + 1][y] = "a"
    # print(maze)
    return maze


def valid(maze, moves, i, j):
    # print("entered valid")
    for move in moves:
        # print(move)
        if move == "l":
            if isBlocked(maze, i, j, "l"):
                # print("false 1")
                return False
            j -= 1
        elif move == "r":
            if isBlocked(maze, i, j, "r"):
                # print("false 2")
                return False
            j += 1
        elif move == "u":
            if isBlocked(maze, i, j, "u"):
                # print("false 3")
                return False
            i -= 1
        elif move == "d":
            if isBlocked(maze, i, j, "d"):
                # print("false 4")
                return False
            i += 1
        return True


def isBlocked(maze, i, j, move):
    x = i
    y = j
    if move == 'u':
        if (x - 1 < 0):
            return True
        if maze[x - 1][y] == 'w':
            return True
        if maze[x - 1][y] == 'bs':
            return True
        if maze[x - 1][y] == 's' and (x - 2 < 0 or
                                      maze[x - 2][y] == 's' or
                                      maze[x - 2][y] == 'bs' or
                                      maze[x - 2][y] == 'w'):
            return True
    elif move == 'd':
        if (x + 1 >= len(maze)):
            return True
        if maze[x + 1][y] == 'w':
            return True
        if maze[x + 1][y] == 'bs':
            return True
        if maze[x + 1][y] == 's' and (x + 2 >= len(maze) or
                                      maze[x + 2][y] == 's' or
                                      maze[x + 2][y] == 'bs' or
                                      maze[x + 2][y] == 'w'):
            return True
        return False
    elif move == 'r':
        if (y + 1 >= len(maze[0])):
            return True
        if maze[x][y + 1] == 'w':
            return True
        if maze[x][y + 1] == 'bs':
            return True
        if maze[x][y + 1] == 's' and (y + 2 >= len(maze[0]) or
                                      maze[x][y + 2] == 's' or
                                      maze[x][y + 2] == 'bs' or
                                      maze[x][y + 2] == 'w'):
            return True
        return False
    elif move == 'l':
        if (y - 1 < 0):
            return True
        # print("elif l ",x,y)
        if maze[x][y - 1] == 'w':
            return True
        if maze[x][y - 1] == 'bs':
            return True
        if maze[x][y - 1] == 's' and (y - 2 < 0 or
                                      maze[x][y - 2] == 's' or
                                      maze[x][y - 2] == 'bs' or
                                      maze[x][y - 2] == 'w'):
            return True
        return False


def isFinished(maze):
    for i in maze:
        for j in i:
            if 's' == j:
                return False
    return True


def bfs(board2D):
    maze = board2D
    visited = set()
    maze_copy = copy.deepcopy(maze)
    nums = queue.Queue()
    nums.put('')
    mazes = queue.Queue()
    mazes.put(maze_copy)
    add = ''
    finished = False
    # print(isFinished(maze))
    while not mazes.empty() and not finished:
        currMaze = mazes.get()
        visited.add(tuple(map(tuple, currMaze)))
        # input()
        # print("------")
        # print(list(currMaze))
        add = nums.get()
        for y, pos in enumerate(currMaze):
            for x, pos2 in enumerate(currMaze[y]):
                if pos2 == "a" or pos2 == "ba":
                    startj = x
                    starti = y
                    break
        # print("agent's place")
        # print(starti,startj)
        for j in ["l", "r", "u", "d"]:
            put = add + j
            if valid(currMaze, j, starti, startj):
                mazes_copy = updateMaze(copy.deepcopy(currMaze), j, starti, startj)
                if tuple(map(tuple, mazes_copy)) not in visited:
                    finished = isFinished(mazes_copy)
                    if finished == True:
                        return list(put)
                    mazes.put(mazes_copy)
                    nums.put(put)
    return list(put)


def dfs(board2D):
    maze = board2D
    maze_copy = copy.deepcopy(maze)
    visited = set()
    nums = queue.LifoQueue()
    nums.put('')
    mazes = queue.LifoQueue()
    mazes.put(maze_copy)
    add = ''
    finished = False
    # print(isFinished(maze))
    while not mazes.empty() and not finished:
        currMaze = mazes.get()
        visited.add(tuple(map(tuple, currMaze)))
        # input()
        # print("------")
        # print(list(currMaze))
        add = nums.get()
        for y, pos in enumerate(currMaze):
            for x, pos2 in enumerate(currMaze[y]):
                if pos2 == "a" or pos2 == "ba":
                    startj = x
                    starti = y
                    break
        # print("agent's place")
        # print(starti,startj)
        for j in ["l", "r", "u", "d"]:
            put = add + j
            if valid(currMaze, j, starti, startj):
                mazes_copy = updateMaze(copy.deepcopy(currMaze), j, starti, startj)
                if tuple(map(tuple, mazes_copy)) not in visited:
                    finished = isFinished(mazes_copy)
                    if finished == True:
                        return list(put)
                    mazes.put(mazes_copy)
                    nums.put(put)
    return list(put)

def find(maze, symbol):
    positions = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == symbol:
                positions.append((i, j))
    return positions
def edgeDeadlockH(maze):
    count = 0
    for i in range(1, len(maze) - 1):
        for j in range(1, len(maze[i]) - 1):
            if maze[i][j] == 's':
                if (maze[i-1][j] == 'w' or maze[i+1][j] == 'w') and (maze[i][j-1] == 'w' or maze[i][j+1] == 'w'):
                    count += 1
    return count*5

def cornerDeadlockH(maze):
    count = 0
    for i in range(1, len(maze) - 1):
        for j in range(1, len(maze[i]) - 1):
            if maze[i][j] == 's':
                if (maze[i-1][j] == 'w' and maze[i][j-1] == 'w') or (maze[i-1][j] == 'w' and maze[i][j+1] == 'w') or (maze[i+1][j] == 'w' and maze[i][j-1] == 'w') or (maze[i+1][j] == 'w' and maze[i][j+1] == 'w'):
                    count += 1
    return count* 5
def heuristic(maze):
    countStones = 0
    # count number of stones
    for i in maze:
        for j in i:
            if 's' == j:
                countStones += 1
    spos = find(maze,'s')
    bpos = find(maze,'b')
    h = 0
    distance2=0
    for s in spos:
        min_distance = float(100000)

        for b in bpos:
            distance = abs(b[0] - s[0]) + abs(b[1] - s[1])
            if distance < min_distance:
                min_distance = distance
        h += min_distance
    apos = findagent(maze)
    x,y = apos
    for s in spos:
        distance2 += abs(x - s[0]) + abs(y - s[1])

    return h + edgeDeadlockH(maze) + cornerDeadlockH(maze) +distance2
def findagent(maze):
    if isinstance(maze,int):
        return None,None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'a' or maze[i][j] == 'ba':
                return i, j
def a_star(board2D):
    maze = board2D
    visited = set()
    maze_copy = copy.deepcopy(maze)
    mazes = queue.PriorityQueue()
    mazes.put((maze_copy,'', 0))
    add = ''
    finished = False
    # print(isFinished(maze))
    while not mazes.empty() and not finished:
        currMaze,currStr,currCost = mazes.get()
        # input()
        # print("------")
        # print(list(currMaze))
        add = currStr
        visited.add(tuple(map(tuple, currMaze)))
        starti,startj = findagent(currMaze)
        # print("agent's place")
        # print(starti,startj)
        for j in ["l", "r", "u", "d"]:
            put = add + j
            if valid(currMaze, j, starti, startj):
                mazes_copy = updateMaze(copy.deepcopy(currMaze), j, starti, startj)
                if tuple(map(tuple, mazes_copy)) not in visited:
                    finished = isFinished(mazes_copy)
                    if finished == True:
                        return list(put)
                    mazes.put((mazes_copy,put,heuristic(mazes_copy)+currCost+1))
    return list(put)
