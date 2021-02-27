import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
alba = inpl()

start = 0
end = N
mid = (end - start) // 2

while start - end <= 0:
    min_front = min(alba[start:mid])
    min_back = min(alba[mid:end])

    min_front *= len(alba[start:mid])
    min_back *= len(alba[mid:end])

    if min_front > min_back:
