import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    len = inp()
    arr = inpl()

    cnt = 0
    for i in range(len - 1):
        big = max(arr[i], arr[i + 1])
        small = min(arr[i], arr[i + 1])
        if big > 2 * small:
            while True:
                cnt += 1
                big = int((big + 1) / 2)
                if big <= 2 * small:
                    break
    print(cnt)