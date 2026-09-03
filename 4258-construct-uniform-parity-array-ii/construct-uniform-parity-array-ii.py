class Solution:
    def uniformArray(self, nums1):
        even = 0
        odd = 0

        for num in nums1:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        # Already all same parity
        if even == 0 or odd == 0:
            return True

        # To make all numbers even or all numbers odd,
        # the smallest element's parity plays an important role.
        smallest = min(nums1)

        if smallest % 2 == 1:
            return True

        return False