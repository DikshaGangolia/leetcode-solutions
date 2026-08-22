class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        dp = {}
        def solve(left, right):
            if left >= right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            ans = 0
            leftSum = 0
            rightSum = prefix[right + 1] - prefix[left]
            for k in range(left, right):
                leftSum += stoneValue[k]
                rightSum -= stoneValue[k]
                if leftSum < rightSum:
                    if ans >= 2 * leftSum:
                        continue
                    ans = max(
                        ans,
                        leftSum + solve(left, k)
                    )
                elif leftSum > rightSum:
                    if ans >= 2 * rightSum:
                        break
                    ans = max(
                        ans,
                        rightSum + solve(k + 1, right)
                    )
                else:
                    ans = max(
                        ans,
                        leftSum + solve(left, k),
                        rightSum + solve(k + 1, right)
                    )
            dp[(left, right)] = ans
            return ans
        return solve(0, n - 1)