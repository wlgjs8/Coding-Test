import sys

def D(n):
    if n * 2 > 9999:
        return 10000
    else:
        return n *2

def S(n):
    if n == 1:
        return 9999
    else:
        return n - 1

def L(n):
    if n < 10:
        return n
    else:
        n = str(n)
        return int(n[1:len(n)] + n[0:1])

def R(n):
    if n < 10:
        return n
    else:
        n = str(n)
        return int(n[len(n)-1:len(n)] + n[0:len(n)-1])

def DSLR(num, ans_num):
    bound = 10000
    visited = [0] * bound
    queue = list()

    queue.append([num, ''])
    while queue:
        now, cmd = queue.pop(0)
        l_now = len(str(now))
        if now == ans_num:
            return cmd

        t = (now * 2) % bound
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'D'))

        t = (now - 1) % bound
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'S'))

        if l_now != 4:
            t = now * 10
        else:
            t, d = divmod(now, 10 ** (l_now - 1))
            t += (d * 10)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'L'))

        if l_now == 1:
            t = now * 1000
        else:
            t, d = divmod(now, 10)
            t += (d * 1000)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'R'))


N = int(sys.stdin.readline())
test = list()
for _ in range(N):
    num, ans_num = list(map(int, sys.stdin.readline().split()))
    test.append([num, ans_num])

for i in range(N):
    num, ans_num = test[i]
    print(DSLR(num, ans_num))
