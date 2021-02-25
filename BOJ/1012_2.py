import sys
from collections import deque

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n and 0 <= ny <= m and visited[nx][ny] == 0:
                if a[nx][ny] == 1:
                    q.appendleft([nx, ny])
                    if a[x][y] == 0:
                        cnt += 1
                else:
                    q.append([nx, ny])

t = inp()
for _ in range(t):
    cnt = 0
    m, n, k = inpl()
    a = [[0] * (m+1) for _ in range(n+1)]
    visited = [[0] * (m+1) for _ in range(n+1)]

    for _ in range(k):
        i, j = inpl()
        a[j+1][i+1] = 1

    bfs(0, 0)
    print(cnt)