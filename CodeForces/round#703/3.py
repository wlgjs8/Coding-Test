import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def avg(list): return int((len(list) + 1) /2) - 1
def sort2(s, e, list):
    cop = list.copy()
    for i in range(s,e):
        for j in range(s, e - i):
            if cop[j] > cop[j+1]:
                cop[j], cop[j+1] = cop[j+1], cop[j]
    return cop[s:e+1]

n, k = inpl()
a = inpl()
a_a = sorted(a)

max_med = a_a[avg(a)]
for i in range(1, n-k+1):
    # med_f = a[i + avg(a[i:])]
    # med_b = a[avg(a[:n-i])]

    b_f = sort2(i, n-1, a)
    med_f = b_f[avg(b_f)]

    b_b = sort2(0, n-i-1, a)
    med_b = b_b[avg(b_b)]
    print(i)
    print(b_f, med_f)
    print(b_b, med_b)
    print()

    med = max(med_f, med_b)
    if max_med < med:
        max_med = med

print(max_med)