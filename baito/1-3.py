import heapq

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, pos = heapq.heappop(q)
        
        if dist[pos] < cost:
            continue
        dist[pos] = cost

        for to, cost2 in box[pos]:
            new_cost = dist[pos] + cost2
            if new_cost < dist[to]:
                dist[to] = new_cost
                heapq.heappush(q, (new_cost, to))

N = 5
box = [[] for _ in range(N)]
edges = [
    (0, 1, 10),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 1, 4),
    (2, 3, 8),
    (2, 4, 2),
    (3, 4, 7),
    (4, 3, 9)
]

for u, v, w in edges:
    box[u].append((v, w))

dist = [10**9]*N

dijkstra(0)

print("最小コスト", dist[N-1])
