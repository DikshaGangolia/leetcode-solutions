class Solution:
    def largestInteger(self, nums, k):
        count = {}
        # Har size-k subarray
        for i in range(len(nums) - k + 1):
            # Current subarray ke unique elements
            seen = set(nums[i:i + k])
            # Har unique element ka subarray count badhao
            for num in seen:
                count[num] = count.get(num, 0) + 1
        # Exactly one subarray mein present numbers
        answer = -1

        for num in count:
            if count[num] == 1:
                answer = max(answer, num)
        return answer