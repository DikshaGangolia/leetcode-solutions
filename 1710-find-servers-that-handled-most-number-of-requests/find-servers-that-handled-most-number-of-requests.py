import heapq
class Solution:
    def busiestServers(self, k, arrival, load):
        INF = k
        size = 1
        while size < k:
            size *= 2
        tree = [INF] * (2 * size)
        for i in range(k):
            tree[size + i] = i
        for i in range(size - 1, 0, -1):
            tree[i] = min(tree[2 * i], tree[2 * i + 1])
        def update(pos, value):
            pos += size
            tree[pos] = value
            pos //= 2
            while pos:
                tree[pos] = min(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
        def query(left, right):
            left += size
            right += size
            result = INF
            while left < right:
                if left % 2:
                    result = min(result, tree[left])
                    left += 1
                if right % 2:
                    right -= 1
                    result = min(result, tree[right])
                left //= 2
                right //= 2
            return result
        busy = []
        handled = [0] * k
        for i in range(len(arrival)):
            current_time = arrival[i]
            while busy and busy[0][0] <= current_time:
                finish, server = heapq.heappop(busy)
                update(server, server)
            start = i % k
            server = query(start, k)
            if server == INF:
                server = query(0, start)
            if server == INF:
                continue
            handled[server] += 1
            update(server, INF)
            heapq.heappush(
                busy,
                (current_time + load[i], server)
            )
        maximum = max(handled)
        return [
            i for i in range(k)
            if handled[i] == maximum
        ]