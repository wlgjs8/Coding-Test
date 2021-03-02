import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
graph = []
INF = 10e10
for _ in range(N):
    a, b, c = inpl()
    if a == 0:
        graph.append((0, c/b))
    elif b == 0:
        graph.append((INF, 0))
    else:
        graph.append((-a/b, -c/b))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if graph[i][0] != graph[j][0]:
            cnt += 1
print(cnt)
