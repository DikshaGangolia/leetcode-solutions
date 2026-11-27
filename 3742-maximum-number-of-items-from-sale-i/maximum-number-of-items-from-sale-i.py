class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_f = 1500
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                for m in range(f, max_f + 1, f):
                    multiples_count[f] += freq[m]
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = budget + 1
        for f, p in items:
            if p < min_price:
                min_price = p
            if p > budget:
                continue
            val = multiples_count[f]  
            for c in range(budget, p - 1, -1):
                if dp[c - p] != -1 and dp[c - p] + val > dp[c]:
                    dp[c] = dp[c - p] + val
        if min_price <= budget:
            for c in range(min_price, budget + 1):
                if dp[c - min_price] != -1 and dp[c - min_price] + 1 > dp[c]:
                    dp[c] = dp[c - min_price] + 1
        return max(dp)