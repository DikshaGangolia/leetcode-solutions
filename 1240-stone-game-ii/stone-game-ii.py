class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        dp = [[-1] * (n + 1) for _ in range(n)]
        def solve(i, M):
            if i >= n:
                return 0
            if dp[i][M] != -1:
                return dp[i][M]
            total = suffix[i]
            best = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                taken = total - suffix[i + X]
                opponent = solve(i + X, max(M, X))
                best = max(best, total - opponent)
            dp[i][M] = best
            return best
        return solve(0, 1)