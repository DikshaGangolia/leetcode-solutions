class Solution:
    def sumGame(self, num):
        n = len(num)
        mid = n // 2
        leftSum = 0
        rightSum = 0
        leftQ = 0
        rightQ = 0
        for i in range(n):
            if i < mid:
                if num[i] == '?':
                    leftQ += 1
                else:
                    leftSum += int(num[i])
            else:
                if num[i] == '?':
                    rightQ += 1
                else:
                    rightSum += int(num[i])
        if (leftQ + rightQ) % 2 == 1:
            return True
        if leftSum - rightSum == (rightQ - leftQ) * 9 // 2:
            return False
        return True
