from collections import deque
class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()  
        cost = 0
        ans = 0
        r = n - 1
        for l in range(n - 1, -1, -1):
            val = nums[l]
            cnt = 1
            while dq and dq[-1][0] <= val:
                prev_val, prev_cnt = dq.pop()
                cost += (val - prev_val) * prev_cnt
                cnt += prev_cnt
            dq.append([val, cnt])
            while cost > k:
                cost -= dq[0][0] - nums[r]
                dq[0][1] -= 1
                if dq[0][1] == 0:
                    dq.popleft()
                r -= 1
            ans += r - l + 1
        return ans