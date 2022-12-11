# Graph = list[list[float]]
from .aliases import Grid

MAX_DISTANCE = 1e7

def min_dist(dist: list[float], processed: list[bool], max_distance: float = MAX_DISTANCE) -> int:
    """Finds the minimum distance between a list of floats, a list of flags, and a maximum distance."""
    min_index = -1
    current_min = max_distance
    for index, value in enumerate(dist):
        if value < current_min and not processed[index]:
            current_min = value
            min_index = index
    return min_index


def dijkstra(graph: Grid, index: int = 0, max_distance: float = MAX_DISTANCE) -> list[float]:
    """Dijkstra formula for finding the shortest path in a given graph."""
    vertex_count = len(graph)
    dist = [max_distance] * vertex_count
    dist[index] = 0
    processed = [False] * vertex_count
    for _ in enumerate(graph):
        min_dist_vertex = min_dist(dist, processed)
        processed[min_dist_vertex] = True
        for current_vertex in range(vertex_count):
            if (
                graph[min_dist_vertex][current_vertex] > 0
                and not processed[current_vertex]
                and dist[current_vertex]
                > dist[min_dist_vertex] + graph[min_dist_vertex][current_vertex]
            ):
                dist[current_vertex] = (
                    dist[min_dist_vertex] + graph[min_dist_vertex][current_vertex]
                )
    return dist