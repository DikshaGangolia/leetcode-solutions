class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        N = n + k - 1
        R = 2 * k
        result = 1
        for i in range(1, R + 1):
            result = result * (N - R + i) // i
        return result % MOD
