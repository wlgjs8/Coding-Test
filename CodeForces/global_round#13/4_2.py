import sys
# from heapq import heappush, heappop
from collections import deque
import math

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

qq = inp()

for _ in range(qq):
    start, end = inpl()
    q = deque()
    q.append(end)
    # heappush(q, end)
    visited = [0] * (max(start, end) + 1)

    check = False
    if start <= end:
        while q:
            cur = q.popleft()
            visited[cur] = 1
            # print(start, cur)
            if cur == start:
                check = True
                break
            elif cur < start:
                break
            for u in range(int(math.sqrt(cur)), cur):
                v = cur - u
                if u & v == v and visited[u] == 0:
                    # print(u, cur)
                    # heappush(q, u)
                    q.append(u)
    print('YES') if check else print('NO')