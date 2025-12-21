K, N, M = map(int, input().split())

graph = {}
for i in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
print(max(graph))
