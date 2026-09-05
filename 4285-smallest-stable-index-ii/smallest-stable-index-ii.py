class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        # Find suffix minimum
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        # Find the first stable index
        for i in range(n):
            if prefix_max - suffix_min[i] <= k:
                return i

            if i + 1 < n:
                prefix_max = max(prefix_max, nums[i + 1])

        return -1