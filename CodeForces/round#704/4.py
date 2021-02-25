import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def differ(list1, list2):
    cnt = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]: cnt += 1
        if cnt > 2: break
    return cnt

copies = list()
n, m = inpl()
for _ in range(n):
    copies.append(inpl())
