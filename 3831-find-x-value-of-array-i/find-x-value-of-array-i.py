class Solution:
    def resultArray(self, nums, k):
        answer = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            # Start a new subarray with only num
            remainder = num % k
            new_dp[remainder] += 1
            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * remainder) % k
                    new_dp[new_remainder] += dp[r]
            dp = new_dp
            # Add current subarrays to final answer
            for r in range(k):
                answer[r] += dp[r]
        return answer