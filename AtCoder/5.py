import sys
from collections import deque
from itertools import combinations

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, x = inpl()
a = inpl()

comb = list()
que = deque()

for i in range(1, n+1):
    comb = list(combinations(a, i))
    for com in comb:
        sum = 0
        for k in com:
            sum += k
        que.append([sum, i])

OK = False
while que:
    sum, time = que.pop()
    if (x-sum) % time == 0:
        print((x -sum)// time)
        OK = True
        break
if not OK:
    print(-1)