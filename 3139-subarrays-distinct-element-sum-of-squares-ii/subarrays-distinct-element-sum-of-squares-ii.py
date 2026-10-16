class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        tree_sum = [0] * size
        tree_sq = [0] * size
        lazy = [0] * size
        def apply(node, left, right, val):
            length = right - left + 1
            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + val * val * length
            ) % MOD
            tree_sum[node] = (
                tree_sum[node] + val * length
            ) % MOD
            lazy[node] += val
        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return
            mid = (left + right) // 2
            val = lazy[node]
            apply(node * 2, left, mid, val)
            apply(node * 2 + 1, mid + 1, right, val)
            lazy[node] = 0
        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return
            push(node, left, right)
            mid = (left + right) // 2
            if ql <= mid:
                update(node * 2, left, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)
            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD
            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD
        last_seen = {}
        ans = 0
        for i, num in enumerate(nums):
            prev = last_seen.get(num, -1)
            update(1, 0, n - 1, prev + 1, i)
            last_seen[num] = i
            ans = (ans + tree_sq[1]) % MOD
        return ans
