parent = list()
rank = list()
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def make_set(i):
    for k in range(i):
        parent.append(k)
        rank.append(0)

def union(n1, n2):
    root1 = find(n1)
    root2 = find(n2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

def solution(n, times):
    answer = n
    make_set(n)
    for row, time in enumerate(times):
        for index in range(len(time)):
            if row != index and times[row][index] == 1:
                if find(row) != find(index):
                    union(row, index)
                    answer -= 1
    # print(parent)
    # print(rank)
    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3,  [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))