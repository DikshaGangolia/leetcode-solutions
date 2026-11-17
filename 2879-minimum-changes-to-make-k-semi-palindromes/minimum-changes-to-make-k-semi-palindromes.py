class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)        
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)        
        def get_cost(i, j):
            L = j - i + 1
            min_changes = float('inf')            
            for d in divisors[L]:
                changes = 0
                group_len = L // d
                for offset in range(d):
                    left = i + offset
                    right = i + offset + (group_len - 1) * d
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
            return min_changes
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)        
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0        
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] + cost[j][i - 1] < dp[p][i]:
                        dp[p][i] = dp[p - 1][j] + cost[j][i - 1]                        
        return dp[k][n]