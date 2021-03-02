import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n, u, v = inpl()
    obs = inpl()
    MIN = 10e6 + 1
    for i in range(len(obs) - 1):
        # if i < len(obs) - 1:
        if abs(obs[i] - obs[i+1]) > 1:
            MIN = 0
            break
        elif abs(obs[i] - obs[i+1]) == 1:
            MIN = min(min(u, v), MIN)
        else:
            MIN = min(min(2*v, u + v), MIN)
    print(MIN)