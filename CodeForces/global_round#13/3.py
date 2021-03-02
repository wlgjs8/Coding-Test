import sys
from heapq import heappush, heappop

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    answer = [1] * (n+1)
    tramp = [1] + inpl()

    if tramp == answer:
        MIN = 0
    else:
        MIN = 10e9
        for _ in range(1, len(tramp)):
            cur_tramp = tramp.copy()
            cnt = 0
            while cur_tramp != answer:
                for j in range(1, len(cur_tramp)):
                    if cur_tramp[j] != 1:
                        i = j

                        while i <= n:
                            if cur_tramp[i] > 1:
                                cur_tramp[i] = 1
                            i = cur_tramp[i] + i
                            cnt += 1

            if MIN > cnt:
                MIN = cnt

    print(MIN)
