class Solution(object):
    def sortPermutation(self, nums):
        ans = -1 
        for i in range(len(nums)):
            if nums[i] != i:
                ans &= nums[i]
        return 0 if ans == -1 else ans