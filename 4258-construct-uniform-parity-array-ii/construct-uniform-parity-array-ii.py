class Solution:
    def uniformArray(self, nums1):
        even = 0
        odd = 0
        for num in nums1:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        if even == 0 or odd == 0:
            return True
        smallest = min(nums1)
        if smallest % 2 == 1:
            return True
        return False
