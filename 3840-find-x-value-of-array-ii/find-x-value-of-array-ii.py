class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        tree = [(1, [0] * k) for _ in range(2 * size)]
        def make_leaf(value):
            r = value % k
            cnt = [0] * k
            cnt[r] = 1
            return (r, cnt)
        def merge(left, right):
            lp, lc = left
            rp, rc = right
            product = (lp * rp) % k
            cnt = [0] * k
            for r in range(k):
                cnt[r] += lc[r]
            for r in range(k):
                if rc[r]:
                    new_r = (lp * r) % k
                    cnt[new_r] += rc[r]
            return (product, cnt)
        for i in range(n):
            tree[size + i] = make_leaf(nums[i])
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        def update(pos, value):
            pos += size
            tree[pos] = make_leaf(value)
            pos //= 2
            while pos:
                tree[pos] = merge(
                    tree[2 * pos],
                    tree[2 * pos + 1]
                )
                pos //= 2
        def query(left, right):
            left += size
            right += size
            left_result = (1, [0] * k)
            right_result = (1, [0] * k)
            while left < right:
                if left % 2 == 1:
                    left_result = merge(
                        left_result,
                        tree[left]
                    )
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    right_result = merge(
                        tree[right],
                        right_result
                    )
                left //= 2
                right //= 2
            return merge(left_result, right_result)
        result = []
        for index, value, start, x in queries:
            update(index, value)
            _, cnt = query(start, n)
            result.append(cnt[x])
        return result
