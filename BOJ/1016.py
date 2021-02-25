import sys

def inpl(): return list(map(int, sys.stdin.readline().split()))
MIN, MAX = inpl()

num = [False] * (MAX - MIN + 2)
count = MAX - MIN + 1
N = 2

while N ** 2  <= MAX:
    i = MIN // (N ** 2)
    if MIN % (N ** 2) != 0:
        i += 1

    while (N ** 2) * i <= MAX:
        idx = (N ** 2) * i - MIN

        if not num[idx]:
            count -= 1
            num[idx] = True
        i += 1
    N += 1

print(count)