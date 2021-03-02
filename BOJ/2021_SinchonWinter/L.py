import sys
from collections import deque

def printList(A : list):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end='')
        print()
    print()
N = int(sys.stdin.readline())
a = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]
pos = [[1] * N for _ in range(N)]
q = deque()
for i in range(N):
    a.append(list(sys.stdin.readline().strip()))
    for j in range(N):
        if a[i][j] == 'O':
            q.append([i, j])

while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for i in range(4):
        nx = x
        ny = y

        cnt = 0
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and a[nx][ny] == '.':
                visited[nx][ny] = 1
                pos[nx][ny] = 0
                cnt += 1
            else:
                break
        print(x, y, nx, ny, cnt)
for i in range(N):
    for j in range(N):
        if a[i][j] == '.' and pos[i][j] == 1:
            a[i][j] = 'B'

# printList(visited)
printList(a)