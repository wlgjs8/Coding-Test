import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    raw_players = inpl()

    players = sorted(raw_players)
    biggest_player = players[n-1]
    impossible = True
    pos = 0
    cur = 0

    sum = 0
    while impossible:
        player = sum + players[cur]
        for i in range(cur+1, n):
            if player >= players[i]:
                player += players[i]
            else:
                break

        if player >= biggest_player:
            pos = cur
            impossible = False
            break
        sum += players[cur]
        cur += 1

    pos = players[pos]

    pos_player = list()
    for i in range(n):
        if players[i] >= pos:
            pos_player.append(players[i])
    print(len(pos_player))

    for i in range(n):
        if raw_players[i] in pos_player:
            print(i+1, end=' ')
    print()