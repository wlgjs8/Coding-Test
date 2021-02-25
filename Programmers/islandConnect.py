parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def make_set(node):
    parent[node] = node
    rank[node] = 0

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

def solution(n, costs):
    answer = 0
    mst = []
    costs.sort(key=lambda x: x[2])

    for node in range(n):
        make_set(node)

    for cost in costs:
        if find(cost[0]) != find(cost[1]):
            union(cost[0], cost[1])
            mst.append(cost[2])
            answer += cost[2]

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))