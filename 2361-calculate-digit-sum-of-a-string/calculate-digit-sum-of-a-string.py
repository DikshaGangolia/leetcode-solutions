class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            ans = ""
            for i in range(0, len(s), k):
                group = s[i:i+k]
                total = 0
                for ch in group:
                    total += int(ch)
                ans += str(total)
            s = ans
        return s
