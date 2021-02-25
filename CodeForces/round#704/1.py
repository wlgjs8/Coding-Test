import sys
from math import ceil
from decimal import Decimal

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(Decimal, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    p, a, b, c = inpl()
    print(min(ceil(p / a) * a, ceil(p / b) * b, ceil(p / c) * c) - p)
