class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0
        def is_rotation(block, target):
            m = len(block)
            doubled = target + target
            pattern = block
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            j = 0
            for x in doubled[:-1]:
                while j > 0 and x != pattern[j]:
                    j = lps[j - 1]
                if x == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            valid = True
            for start in range(0, n, k):
                block = nums[start:start + k]
                target = sorted_nums[start:start + k]
                if not is_rotation(block, target):
                    valid = False
                    break
            if valid:
                ans += k
        return ans
