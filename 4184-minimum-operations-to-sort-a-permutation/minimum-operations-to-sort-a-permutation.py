class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        k = nums[0]
        INF = float('inf')
        ans = INF
        if all(nums[i] == (i + k) % n for i in range(n)):
            if k == 0:
                ans = 0
            else:
                ans = min(n - k, k + 2)
        if all(nums[i] == (k - i) % n for i in range(n)):
            kp = (k + 1) % n
            if kp == 0:
                cost = 1
            else:
                cost = min(kp + 1, 1 + min(n - kp, kp + 2))
            ans = min(ans, cost)
        return -1 if ans == INF else ans