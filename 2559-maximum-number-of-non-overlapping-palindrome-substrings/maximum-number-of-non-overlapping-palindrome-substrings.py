class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        # pal[i][j] tells whether s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]
        # Length 1
        for i in range(n):
            pal[i][i] = True
        # Length 2 or more
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]
        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # Don't use a palindrome ending here
            dp[i] = dp[i - 1]
            # Try every possible starting position
            for j in range(i):
                length = i - j
                if length >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]