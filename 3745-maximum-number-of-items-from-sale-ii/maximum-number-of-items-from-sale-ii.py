class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for m in range(f, n + 1, f):
                    multiples_count[f] += freq[m]
        items_sorted = sorted(items, key=lambda x: x[1])
        min_price = items_sorted[0][1]
        ans = budget // min_price 
        cur_copies = 0
        rem = budget
        for f, p in items_sorted:
            if rem < min_price:
                break
            cap = multiples_count[f] - 1
            if cap <= 0 or rem < p:
                continue
            max_k = min(cap, rem // p)
            for k in (0, max_k - 1, max_k):
                if 0 <= k <= max_k:
                    cand = cur_copies + 2 * k + (rem - k * p) // min_price
                    if cand > ans:
                        ans = cand
            if p < 2 * min_price:
                cur_copies += 2 * max_k
                rem -= max_k * p
            else:
                break
        return ans