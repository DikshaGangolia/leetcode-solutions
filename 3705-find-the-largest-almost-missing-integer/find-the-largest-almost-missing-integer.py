class Solution:
    def largestInteger(self, nums, k):
        count = {}
        for i in range(len(nums) - k + 1):
            seen = set(nums[i:i + k])
            for num in seen:
                count[num] = count.get(num, 0) + 1
        answer = -1
        for num in count:
            if count[num] == 1:
                answer = max(answer, num)
        return answer
