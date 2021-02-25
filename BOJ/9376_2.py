import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    visited = [[0] * w for _ in range(h)]

    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = 1

        print(x, y, cnt)
        if x == 0 or y == 0 or x == h or y == w:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                if a[nx][ny] == '.':
                    q.appendleft([nx, ny, cnt])
                elif a[nx][ny] == '#':
                    a[nx][ny] = '.'
                    q.append([nx, ny, cnt + 1])

tc = int(input())
while tc:
    h, w = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    q = deque()

    # new_map()
    temp = []
    for i in range(h):
        for j in range(w):
            if a[i][j] == '$':
                temp.extend([i, j])
                a[i][j] = '.'

    q.append([temp[0], temp[1], 0])
    q.append([temp[2], temp[3], bfs(temp[0], temp[1])])

    print(bfs(temp[2], temp[3]))
    tc -= 1
