import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, q = inpl()
a = inpl()

sorted_a = sorted(a, reverse=True)
if 0 not in sorted_a:
    first_zero = n + 1
else:
    first_zero = sorted_a.index(0) + 1

for _ in range(q):
    t, k = inpl()
    if t == 1:
        a[k-1] = 1 - a[k-1]
        if a[k-1] == 1:
            first_zero += 1
        else:
            first_zero -= 1
    else:
        # print('first_zero : ', first_zero)
        if k >= first_zero:
            print(0)
        else:
            print(1)
