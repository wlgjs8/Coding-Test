from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dx, dy = [-1,1,0,0],[0,0, -1, 1]

que = [(0,0)]
visited[0][0] = 1

while que:
    x, y = que.pop(0)

    if x == N-1 and y == M-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
