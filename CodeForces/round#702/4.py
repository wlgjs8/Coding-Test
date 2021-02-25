import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    per_a = inpl()
    per_depth = [0 for _ in range(n)]

    if n > 1:
        root = max(per_a)
        root_index = per_a.index(root)
        que = list()

        if root_index == 0:
            que.append([1, n-1, 0])
        elif root_index == n - 1:
            que.append([0, n-2, 0])
        else:
            que.append([0, root_index-1, 0])
            que.append([root_index+1, n-1, 0])


        while que:
            start, end, depth = que.pop(0)

            if end == start:
                per_depth[start] = depth + 1

            else:
                node_max = 0
                for i in range(start, end+1):
                    if node_max < per_a[i]:
                        node_max = per_a[i]
                max_index = per_a.index(node_max)
                per_depth[max_index] = depth + 1

                if max_index == start:
                    que.append([start+1, end, depth + 1])
                elif max_index == end:
                    que.append([start, end-1, depth + 1])
                else:
                    que.append([start, max_index-1, depth + 1])
                    que.append([max_index-1, end, depth + 1])

        print(' '.join(repr(e) for e in per_depth))
    else:
        print(0)