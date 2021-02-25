import sys

def BFS(x, y):
    global answer
    queue = set([(x, y, board[x][y])])

    while queue:
        x, y, ans = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                queue.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans) + 1)

# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]

R, C = 2, 4
board = [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 1
BFS(0, 0)
print(answer)

