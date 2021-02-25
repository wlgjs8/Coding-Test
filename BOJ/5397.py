import sys

def inp(): return int(sys.stdin.readline())

t = inp()
for _ in range(t):
    str = sys.stdin.readline().strip()
    cursor = 0
    pwd = list()
    for char in str:
        if char == '<':
            cursor -= 1
            if cursor < 0:
                cursor = 0
        elif char == '>':
            cursor += 1
            if cursor > len(pwd):
                cursor = len(pwd)
        elif char == '-':
            if len(pwd) > 1:
                pwd.pop()
                cursor -= 1
        else:
            pwd.insert(cursor, char)
            cursor += 1

    for p in pwd:
        print(p, end='')