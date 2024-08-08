import heapq

def dijkstra(graph, source, target):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    min_heap = [(0, source)]
    prev = {node: None for node in graph}  # For path reconstruction

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            if weight < 0:
                continue  # Skip construction roads
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distances[target], prev

def modify_road_times(nodes, edges, source, destination, target_time):
    graph = {node: {} for node in range(nodes)}
    construction_edges = []

    for u, v, w in edges:
        if w == -1:
            construction_edges.append((u, v))
        else:
            graph[u][v] = w
            graph[v][u] = w

    initial_time, _ = dijkstra(graph, source, destination)

    if initial_time == target_time:
        return [[u, v, w] for u, v, w in edges]

    low, high = 1, 2 * 10**9
    while low < high:
        mid = (low + high) // 2

        for u, v in construction_edges:
            graph[u][v] = graph[v][u] = mid

        current_time, _ = dijkstra(graph, source, destination)

        for u, v in construction_edges:
            del graph[u][v]
            del graph[v][u]

        if current_time < target_time:
            low = mid + 1
        else:
            high = mid

    final_weight = low

    for u, v in construction_edges:
        graph[u][v] = graph[v][u] = final_weight

    return [[u, v, w] for u, v, w in edges]
