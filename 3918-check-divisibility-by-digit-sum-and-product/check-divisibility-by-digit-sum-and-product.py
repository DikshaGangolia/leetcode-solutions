class Solution:
    def checkDivisibility(self, n):
        num = n
        digit_sum = 0
        digit_product = 1
        while num > 0:
            digit = num % 10
            digit_sum = digit_sum + digit
            digit_product = digit_product * digit
            num = num // 10
        total = digit_sum + digit_product
        return n % total == 0