import sys
from collections import deque

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, M = inpl()
a = []
sharks = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    temp = inpl()
    a.append(temp)
    for j in range(M):
        if temp[j] == 1:
            sharks.append([i, j])

q = deque()
q.append([0, 0])

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

MAX = 0
cnt = 0
while q:
    x, y = q.popleft()
    visited[x][y] = 1

    MIN = []
    for shark in sharks:
        # xd, yd = 0, 0
        # if abs(x - shark[0]) +  abs(y - shark[1]) > 0:
        MIN.append(abs(x - shark[0]) +  abs(y - shark[1]))
        # MIN.append(xd + yd)

    if MAX <= min(MIN):
        MAX = min(MIN)
        # print(x, y)
        cnt +=1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            q.append([nx, ny])
print(MAX)
print(cnt)
