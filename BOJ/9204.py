import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def canMove(s,ss,e,ee):
    if abs(al.index(s) - al.index(e)) == abs(ss - ee):
        return True
    else: return False
t = inp()
for _ in range(t):
    a1, n1, a2, n2 = sys.stdin.readline().split()
    n1, n2 = int(n1), int(n2)
    al = [' ','A','B','C','D','E','F','G','H']

    if (al.index(a1) - n1) % 2 != (al.index(a2) - n2) % 2:
        print('Impossible')
        continue
    if a1 == a2 and n1 == n2:
        print(0, a1, n1)
        continue
    elif canMove(a1, n1, a2, n2):
        print(1, a1, n1, a2, n2)
        continue
    else:
        check = False
        for i in range(1, 9):
            for j in range(1, 9):
                # print(i, j)
                if canMove(a1,n1,al[i],j) and canMove(al[i],j,a2,n2):
                    print(2, a1, n1, al[i], j, a2, n2)
                    check = True
                    break
            if check:
                break