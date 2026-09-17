class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        # best[i] = minimum length of a valid subarray
        # completely inside arr[0...i]
        best = [float('inf')] * n
        left = 0
        curr_sum = 0
        answer = float('inf')
        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            if right > 0:
                best[right] = best[right - 1]
            if curr_sum == target:
                length = right - left + 1
                # Previous subarray must end before 'left'
                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])
                # Current subarray becomes a candidate for future subarrays
                best[right] = min(best[right], length)
        if answer == float('inf'):
            return -1
        return answer