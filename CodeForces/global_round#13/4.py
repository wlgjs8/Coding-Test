import sys
from heapq import heappush, heappop

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

qq = inp()
n = 10
graph = [[] for _ in range(n + 1)]

for sum in range(1, n + 1):
    for u in range(1, sum):
        v = sum - u
        if u & v == v:
            graph[u].append(sum)


for _ in range(qq):
    start, end = inpl()
    q = []
    heappush(q, start)

    check = False
    while q:
        cur = heappop(q)

        if cur == end:
            check = True
        elif cur > end:
            break

        for i in graph[cur]:
            heappush(q, i)
    print('YES') if check else print('NO')

print(graph)
print(graph[2])
