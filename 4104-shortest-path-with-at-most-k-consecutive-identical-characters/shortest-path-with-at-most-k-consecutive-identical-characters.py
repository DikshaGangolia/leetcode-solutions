
import heapq
class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        pq = [(0, 0, labels[0], 1)]
        dist = {}
        while pq:
            cost, node, last, count = heapq.heappop(pq)
            state = (node, last, count)
            if state in dist:
                continue
            dist[state] = cost
            if node == n - 1:
                return cost
            for nei, weight in graph[node]:
                if labels[nei] == last:
                    new_count = count + 1
                else:
                    new_count = 1
                if new_count <= k:
                    new_state = (nei, labels[nei], new_count)
                    if new_state not in dist:
                        heapq.heappush(
                            pq,
                            (cost + weight, nei, labels[nei], new_count)
                        )
        return -1
