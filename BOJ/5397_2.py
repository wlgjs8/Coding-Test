import sys

def inp(): return int(sys.stdin.readline())

t = inp()
for _ in range(t):
    left = []
    right = []
    pwd = sys.stdin.readline().strip()

    for x in pwd:
        if x == '>':
            if right:
                left.append(right.pop())
        elif x == '<':
            if left:
                right.append(left.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)
    print("".join(left) + "".join(reversed(right)))
