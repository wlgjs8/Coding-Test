import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().strip()))

def dfs(a, b):
    visited[a][b] = 1
    global nums
    if matrix[a][b] == 1:
        nums += 1
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny)

N = inp()
matrix = list()
visited = [[0] * N for _ in range(N)]

for i in range(N):
    matrix.append(inpl())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

numlist = list()
nums = 0
for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b)
            numlist.append(nums)
            nums = 0

print(len(numlist))
numlist.sort()
for num in numlist:
    print(num)