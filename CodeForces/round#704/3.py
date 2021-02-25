import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, m = inpl()
s = sys.stdin.readline()
t = sys.stdin.readline()
ex_start = 0
max = 0
for i in range(m):
    start = s.find(t[i])
    ex_end = start - 1

    if max < ex_end - ex_start + 1:
        max = ex_end - ex_start + 1

    ex_start = start
    print(start, ex_start, ex_end)


# if n - end > max:
#     max = n - end

if max == n:
    max = n - 1
print(max)