import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if a[x][y] == 0 and a[nx][ny] == 1:
                cnt += 1
                bfs(nx,ny)
            else:
                bfs(nx,ny)
    return

t = inp()
for _ in range(t):
    cnt = 0
    m, n, k = inpl()
    a = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        i, j = inpl()
        a[j][i] = 1

    bfs(0, 0)
    print(cnt)
    #
    # for i in range(n):
    #     for j in range(m):
    #         print(a[i][j], end='')
    #     print()
    #
    # print()
    # for i in range(n):
    #     for j in range(m):
    #         print(visited[i][j], end='')
    #     print()
