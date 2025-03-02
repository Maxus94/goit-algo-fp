import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    shortest_paths = {vertex: [] for vertex in graph}
    shortest_paths[start] = [start]    
 
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)             
        if current_distance <= distances[current_vertex]:       
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight            
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = shortest_paths[current_vertex] + [neighbor]
                    heapq.heappush(pq, (distance, neighbor))    
    return distances, shortest_paths

graph = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('D', 3)],
    'C': [('A', 10), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 4)],
    'E': [('D', 4)]
}

print(dijkstra(graph, "A"))
