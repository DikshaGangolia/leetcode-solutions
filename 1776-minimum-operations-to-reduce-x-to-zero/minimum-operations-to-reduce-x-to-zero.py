class Solution:
    def minOperations(self, nums, x):
        n = len(nums)

        total = sum(nums)
        target = total - x

        # No elements need to remain
        if target == 0:
            return n

        # Impossible to get a subarray with negative sum
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(n):
            current_sum += nums[right]

            # Shrink window if sum becomes too large
            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if current_sum == target:
                max_length = max(
                    max_length,
                    right - left + 1
                )

        if max_length == -1:
            return -1

        return n - max_length