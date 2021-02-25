import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

# def show_maze(maze):
#     global h, w
#     for i in range(h):
#         for j in range(w):
#             print(chr(maze[i][j]), end='')
#         print()

def bfs(x,y):
    global cnt
    global h, w
    visited[x][y] = 1

    if x == 0 or y == 0 or x == h or y == w:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
            if maze[nx][ny] == ord('.'):
                return bfs(nx, ny)
            elif maze[nx][ny] == ord('#'):
                maze[nx][ny] = ord('.')
                cnt += 1
                return bfs(nx,ny)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = inp()
for _ in range(t):
    maze = []
    h, w = inpl()
    prisoners = []

    for i in range(h):
        temp = sys.stdin.readline().strip()
        tmp = list()
        for j in range(w):
            tmp.append(ord(temp[j]))
            if ord(temp[j]) == ord('$'):
                prisoners.append((i, j))

        maze.append(tmp)

    cnt = 0
    for prisoner in prisoners:
        visited = [[0] * w for _ in range(h)]
        bfs(prisoner[0], prisoner[1])
    print(cnt)
