class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0:
            return False

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]
                if j > 0:
                    prev |= dp[i][j - 1]

                for b in prev:
                    if grid[i][j] == '(':
                        new_b = b + 1
                    else:
                        new_b = b - 1

                    if new_b < 0:
                        continue

                    remaining = (m - 1 - i) + (n - 1 - j)

                    if new_b <= remaining:
                        dp[i][j].add(new_b)

        return 0 in dp[m - 1][n - 1]