class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        max_len = 2  
        max_limit = 25200
        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]
            for j in range(i + 1, n):
                val = nums[j]
                prod *= val
                if prod > max_limit:
                    break
                g = gcd(g, val)
                l = (l * val) // gcd(l, val)
                if prod == l * g:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
        return max_len