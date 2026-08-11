class Solution:
    def missingInteger(self, nums):
        # Step 1: Find sum of longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        # Step 2: Find smallest missing number >= total
        x = total
        while x in nums:
            x += 1
        return x
