class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
        digits = []
        for i in range(num):
            digit = min(9, sum)
            digits.append(str(digit))
            sum -= digit
        return ''.join(digits)