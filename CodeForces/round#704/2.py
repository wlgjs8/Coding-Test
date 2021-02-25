import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def max_index(s,e):
    max = 0
    maxi = 0
    for i in range(s, e):
        if deck1[i] > max:
            max = deck1[i]
            maxi = i
    return maxi

t = inp()
for _ in range(t):
    n = inp()
    deck1 = inpl()
    deck2 = list()
    end_index = n

    while len(deck2) != n:
        max_card_index = max_index(0, end_index)
        deck2.extend(deck1[max_card_index:])
        deck1 = deck1[:max_card_index]
        end_index = max_card_index

    print(*deck2)