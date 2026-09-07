class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007
        last = [0] * 26
        total = 1
        for ch in s:
            index = ord(ch) - ord('a')
            new_total = (total * 2 - last[index]) % MOD
            last[index] = total
            total = new_total
        return (total - 1) % MOD