import sys
from collections import deque

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark = 2
    eat = 0
    eat_flag = False
    answer = 0

    while q:
        size = len(q)
        q = deque(sorted(q))

        for _ in range(size):
            x, y = q.popleft()

            if board[x][y] != 0 and board[x][y] < shark:
                eat += 1
                board[x][y] = 0

                if eat == shark:
                    shark += 1
                    eat = 0

                q, visited = deque(), set([(x, y)])
                eat_flag = True

                answer = time

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            if eat_flag:
                eat_flag = False
                break
        time += 1

    return answer

n = inp()
board = [inpl() for _ in range(n)]

# 1. 초기 상어(자신)의 위치를 파악하고, 해당 자리는 판에서 비워둔다.
s_x, s_y = None, None
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0

print(bfs(s_x, s_y))
