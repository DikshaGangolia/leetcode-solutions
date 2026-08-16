class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        a = count[0]
        b = count[1]
        c = count[2]

        if a % 2 == 0:
            return b > 0 and c > 0

        return abs(b - c) > 2