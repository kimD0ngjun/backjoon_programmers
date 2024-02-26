class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        
        for i in range(1, n+1):
            graph[i]
        
        for lst in times:
            graph[lst[0]][lst[1]] = lst[2]
        
        min_times = self.dijkstra(graph, k) 
        
        if sys.maxsize in min_times.values():
            return -1
        else:
            return max(min_times.values())  
    
    def dijkstra(self, graph, start):
        inf = sys.maxsize
        min_distances = {vertex: inf for vertex in graph} 
        min_distances[start] = 0

        queue = [] 

        heapq.heappush(queue, (min_distances[start], start))

        while queue:
            cur_distance, cur_dir_vertex = heapq.heappop(queue)

            if min_distances[cur_dir_vertex] < cur_distance:
                continue

            for adj_vertex, weight in graph[cur_dir_vertex].items():
                updated_distance = cur_distance + weight

                if updated_distance < min_distances[adj_vertex]:
                    min_distances[adj_vertex] = updated_distance
                    heapq.heappush(queue, (updated_distance, adj_vertex))

        return min_distances
