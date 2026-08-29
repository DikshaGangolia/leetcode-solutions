class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original_index)
        pairs = []

        for i in range(n):
            pairs.append((nums[i], i))

        # Sort according to values
        pairs.sort()

        answer = nums[:]

        start = 0

        while start < n:
            end = start

            # Find all elements belonging to the same group
            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            # Get values and their original indices
            values = []
            indices = []

            for i in range(start, end + 1):
                values.append(pairs[i][0])
                indices.append(pairs[i][1])

            # Put smallest values at smallest indices
            indices.sort()

            for i in range(len(indices)):
                answer[indices[i]] = values[i]

            # Move to next group
            start = end + 1

        return answer