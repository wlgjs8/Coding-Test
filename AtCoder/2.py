import sys

def inp(): return sys.stdin.readline()
def inpl(): return list(map(int, sys.stdin.readline().split()))

str = inp()
lower_str = str.lower()
upper_str = str.upper()
OK = True
for i in range(len(str)):
    if i % 2 == 0:
        if str[i] != lower_str[i]:
            OK = False
            break
    else:
        if str[i] != upper_str[i]:
            OK = False
            break
if OK: print('Yes')
else: print('No')