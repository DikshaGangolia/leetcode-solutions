class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diff) <= k:
            return 0
        low = 0
        high = max(diff)
        while low < high:
            mid = (low + high) // 2
            operations = sum(max(d - mid, 0) for d in diff)
            if operations <= k:
                high = mid
            else:
                low = mid + 1
        level = low
        operations = sum(max(d - level, 0) for d in diff)
        remaining = k - operations
        result = sum(min(d, level) ** 2 for d in diff)
        result -= remaining * (2 * level - 1)
        return result
