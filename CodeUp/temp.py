import sys

R, C = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]
visited = [[0] * C for _ in range(R)]

que = list()
que.append([0, 0])
visited[0][0] = 1

while que:
    x, y = que.pop(0)

    if x == R-1 and y == C-1:
        print(visited[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ((0 <= nx < R) and (0 <= ny < C)) and maze[nx][ny] != '0' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            que.append([nx, ny])
