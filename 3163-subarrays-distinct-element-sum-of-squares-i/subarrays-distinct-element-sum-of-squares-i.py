class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                ans += count * count
        return ans
