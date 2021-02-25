import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
e = inp()
coms = [[0] * (n+1) for _ in range(n + 1)]

for _ in range(e):
    i, j = inpl()
    if i > j:
        coms[j][i] = 1
    else:
        coms[i][j] = 1

visited = [0 for _ in range(n+1)]
visited[1] = 1

cnt = 0
connected_com = set()
connected_com.add(1)
while connected_com:
    index = connected_com.pop()
    for i in range(1, n+1):
        if coms[index][i] == 1 and visited[i] == 0:
            visited[i] = 1
            connected_com.add(i)
            cnt += 1
print(cnt)