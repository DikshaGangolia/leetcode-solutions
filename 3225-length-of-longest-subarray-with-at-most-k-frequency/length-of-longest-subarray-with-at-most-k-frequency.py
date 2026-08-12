class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        max_length = 0
        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            # Shrink window if frequency becomes greater than k
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        return max_length