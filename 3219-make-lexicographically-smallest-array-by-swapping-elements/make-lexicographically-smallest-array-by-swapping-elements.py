class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        pairs = []
        for i in range(n):
            pairs.append((nums[i], i))
        pairs.sort()
        answer = nums[:]
        start = 0
        while start < n:
            end = start
            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1
            values = []
            indices = []
            for i in range(start, end + 1):
                values.append(pairs[i][0])
                indices.append(pairs[i][1])
            indices.sort()
            for i in range(len(indices)):
                answer[indices[i]] = values[i]
            start = end + 1
        return answer
