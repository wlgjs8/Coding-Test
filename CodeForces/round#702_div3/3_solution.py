t = int(input())
while (t):
    x = int(input())
    curr = 1
    possible = False
    while (curr**3 <= x):
        rep = x - curr**3
        temp = int(round(rep**(1/3)))
        if (rep >= 1 and temp**3 == rep):
            possible = True
            break
        curr += 1
    print("YES" if (possible) else "NO")
    t -= 1