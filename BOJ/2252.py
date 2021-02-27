import sys
from collections import deque

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, M = inpl()
tree = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = inpl()
    tree[a].append(b)
    inDegree[b] += 1

q = deque()
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    a = q.popleft()
    print(a, end=' ')
    for i in tree[a]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)