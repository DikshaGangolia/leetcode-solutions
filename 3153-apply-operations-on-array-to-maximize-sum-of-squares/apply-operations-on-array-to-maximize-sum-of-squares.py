class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_count = [0] * 30
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    bit_count[bit] += 1
        ans = 0
        for _ in range(k):
            x = 0
            for bit in range(30):
                if bit_count[bit] > 0:
                    x |= (1 << bit)
                    bit_count[bit] -= 1
            ans = (ans + x * x) % MOD
        return ans
