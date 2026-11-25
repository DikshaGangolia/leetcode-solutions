import random
class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        if 1 in freq.values():
            return 1
        if len(freq) == 1:
            return n
        M1 = 1000000007
        M2 = 1000000009
        B1 = random.randint(100007, 1000000006)
        B2 = random.randint(100007, 1000000006)
        def has_unique(L):
            if L == n:
                return True
            h1 = 0
            h2 = 0
            for i in range(L):
                x = nums[i]
                h1 = (h1 * B1 + x) % M1
                h2 = (h2 * B2 + x) % M2
            hashes = [(h1 << 32) | h2]
            p1 = pow(B1, L - 1, M1)
            p2 = pow(B2, L - 1, M2)
            for i in range(L, n):
                out_x = nums[i - L]
                in_x = nums[i]
                h1 = ((h1 - out_x * p1) * B1 + in_x) % M1
                h2 = ((h2 - out_x * p2) * B2 + in_x) % M2
                hashes.append((h1 << 32) | h2)
            hashes.sort()
            m = len(hashes)
            if hashes[0] != hashes[1] or hashes[-1] != hashes[-2]:
                return True
            for i in range(1, m - 1):
                if hashes[i] != hashes[i - 1] and hashes[i] != hashes[i + 1]:
                    return True
            return False
        lo, hi = 2, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans