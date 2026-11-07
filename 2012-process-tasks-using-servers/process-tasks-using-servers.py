import heapq
class Solution:
    def assignTasks(self, servers, tasks):
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0
        for j in range(len(tasks)):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))
            weight, index = heapq.heappop(free)
            ans.append(index)
            finish_time = time + tasks[j]
            heapq.heappush(
                busy,
                (finish_time, weight, index)
            )
        return ans
