class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted([x * x for x in nums])
        n = len(squares)
        positive_count = (n + 1) // 2
        return sum(squares[n - positive_count:]) - sum(squares[:n - positive_count])
