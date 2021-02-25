import sys
import timeit

def test():
    t = 1
    # t = int(sys.stdin.readline())
    for _ in range(t):
        # n, k = list(map(int, sys.stdin.readline().split()))
        n, k = 1000000, 999999
        cnt = 0
        for i in range(k):
            A = (n - (i % n))
            B = ((cnt % n) + 1)
            if A == B:
                cnt += 1
            cnt += 1

        print((cnt - 1) % n + 1)
    return

t1 = timeit.timeit('test()', setup='from __main__ import test', number=1)
print(t1)