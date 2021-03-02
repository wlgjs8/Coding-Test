import sys

N = int(sys.stdin.readline())
graph = []
INF = 10e9 + 1
for _ in range(N):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if b == 0:
        graph.append(INF)
    else:
        graph.append(a/b)

cnt = int(N * (N-1) / 2)
mtt = []
graph.sort()
graphcnt = 1
for i in range(N-1):
    if graph[i] != graph[i+1]:
        mtt.append(graphcnt)
        graphcnt = 1
    else:
        graphcnt += 1
mtt.append(graphcnt)
for mt in mtt:
    cnt -= int(mt * (mt-1)/2)

print(cnt)
