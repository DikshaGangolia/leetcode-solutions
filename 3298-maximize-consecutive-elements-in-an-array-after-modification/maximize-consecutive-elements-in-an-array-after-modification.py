from collections import defaultdict
class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = defaultdict(int)
        for num in nums:
            dp[num + 1] = dp[num] + 1
            dp[num] = dp[num - 1] + 1           
        return max(dp.values())