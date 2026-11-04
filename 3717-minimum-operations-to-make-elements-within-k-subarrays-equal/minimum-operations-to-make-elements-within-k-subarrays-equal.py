class Fenwick:
    def __init__(self, n):
        self.n = n
        self.count = [0] * (n + 1)
        self.total = [0] * (n + 1)
    def update(self, i, c, s):
        while i <= self.n:
            self.count[i] += c
            self.total[i] += s
            i += i & -i
    def query(self, bit, i):
        result = 0
        while i > 0:
            result += bit[i]
            i -= i & -i
        return result
    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = idx + step
            if nxt <= self.n and self.count[nxt] < k:
                k -= self.count[nxt]
                idx = nxt
            step >>= 1
        return idx + 1
class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        values = sorted(set(nums))
        size = len(values)
        rank = {v: i + 1 for i, v in enumerate(values)}
        bit = Fenwick(size)
        window_sum = 0
        for i in range(x):
            bit.update(rank[nums[i]], 1, nums[i])
            window_sum += nums[i]
        costs = []
        for start in range(n - x + 1):
            mid = bit.kth((x + 1) // 2)
            median = values[mid - 1]
            left_count = bit.query(bit.count, mid)
            left_sum = bit.query(bit.total, mid)
            right_count = x - left_count
            right_sum = window_sum - left_sum
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )
            costs.append(cost)
            if start < n - x:
                outgoing = nums[start]
                incoming = nums[start + x]
                bit.update(rank[outgoing], -1, -outgoing)
                bit.update(rank[incoming], 1, incoming)
                window_sum += incoming - outgoing
        INF = float('inf')
        prev = [0] * (n + 1)
        for t in range(1, k + 1):
            curr = [INF] * (n + 1)
            for i in range(1, n + 1):
                curr[i] = curr[i - 1]
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )
            prev = curr
        return prev[n]
