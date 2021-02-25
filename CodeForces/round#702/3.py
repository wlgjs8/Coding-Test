import sys

N = 1000000000000
def inp(): return int(sys.stdin.readline())
cubes = list()

def precalc():
    i = 1
    while i*i*i <= N:
        cubes.append(i*i*i)
        i+=1

t = inp()
precalc()
for _ in range(t):
    x = inp()
    check = False
    i = 1
    while i*i*i <= x:
        if (x-i**3) in cubes:
            print('YES')
            check = True
            break
        i += 1

    if check == False:
        print('No')


