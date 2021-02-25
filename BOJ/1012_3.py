import sys
from collections import deque
sys.setrecursionlimit(10**4)

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # global cnt
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        fcnt = 0

        if 0 <= nx <= n and 0 <= ny <= m and visited[nx][ny] == 0:
            if a[nx][ny] == 1:
                bfs(nx, ny)

        fcnt += 1
        if fcnt == 4:
            return

t = inp()
for _ in range(t):
    m, n, k = inpl()
    a = [[0] * (m+1) for _ in range(n+1)]
    visited = [[0] * (m+1) for _ in range(n+1)]

    q = deque()
    for _ in range(k):
        i, j = inpl()
        a[j+1][i+1] = 1
        q.append([j+1, i+1])

    cnt = 0
    while q:
        x, y = q.popleft()

        if visited[x][y] == 0:
            bfs(x, y)
            cnt += 1

    print(cnt)