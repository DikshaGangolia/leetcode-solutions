class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i
        intervals = []
        # Find the smallest valid interval for every character
        for c in range(26):
            if last[c] == -1:
                continue
            left = first[c]
            right = last[c]
            valid = True
            i = left
            while i <= right:
                x = ord(s[i]) - ord('a')
                # This character appeared before our interval
                if first[x] < left:
                    valid = False
                    break
                # Expand interval if necessary
                right = max(right, last[x])
                i += 1
            if valid:
                intervals.append((left, right))
        # Sort by ending position
        intervals.sort(key=lambda x: x[1])
        result = []
        prev_end = -1
        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right
        return result