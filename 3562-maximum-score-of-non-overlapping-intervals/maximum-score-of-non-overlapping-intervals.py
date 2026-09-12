class Solution:
    def maximumWeight(self, intervals):
        import bisect
        n = len(intervals)
        # Add original index
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])
        # Sort by start, then end, etc.
        arr.sort()
        # Starting positions
        starts = [x[0] for x in arr]
        # next[i] = first interval whose start > arr[i]'s end
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])
        # dp[i][k] = best answer from i onward
        # when we can select at most k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                # Option 1: skip current interval
                skip_score, skip_indices = dp[i + 1][k]
                # Option 2: take current interval
                take_score, take_indices = dp[nxt[i]][k - 1]
                take_score += arr[i][2]
                take_indices = tuple(
                    sorted(take_indices + (arr[i][3],))
                )
                # Choose better option
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    # Same score → lexicographically smaller
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)
        return list(dp[0][4][1])