import sys
from itertools import combinations

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

L, C = inpl()
c = sys.stdin.readline().split()

vow = {'a', 'e', 'i', 'o', 'u'}

c.sort()
cases = list(combinations(c, L))

for case in cases:
    vow_cnt = len(set(case)&vow)
    if vow_cnt >= 1 and vow_cnt <= L - 2:
        print(''.join(case))