import sys
from heapq import heappop, heappush

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, M = inpl()
tree = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = inpl()
    tree[a].append(b)
    inDegree[b] += 1

heap = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        heappush(heap, i)

answer = []
while heap:
    problem = heappop(heap)
    answer.append(problem)
    for i in tree[problem]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heappush(heap, i)
print(*answer)