def dfs(node):
    visit[node] = 1
    print(node, end=' ')

    for i in range(1, N + 1):
        if not visit[i] and graph[node][i] == 1:
            dfs(i)

    return visit

def bfs(node):
    queue = list()
    queue.append(node)
    visit[node] = 0

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for i in range(1, N+1):
            if visit[i] and graph[node][i] == 1:
                queue.append(i)
                visit[i] = 0

    return visit

N, V, start_node = list(map(int, input().split()))
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(V):
    n1, n2 = list(map(int, input().split()))
    graph[n1][n2] = graph[n2][n1] = 1

visit = [0] * (N+1)

dfs(start_node)
print()
bfs(start_node)