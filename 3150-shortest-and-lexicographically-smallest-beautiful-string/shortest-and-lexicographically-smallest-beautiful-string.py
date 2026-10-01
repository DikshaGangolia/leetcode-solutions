class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        ans = ""
        for i in range(n):
            count = 0
            for j in range(i, n):
                if s[j] == '1':
                    count += 1
                if count == k:
                    temp = s[i:j + 1]
                    if ans == "":
                        ans = temp
                    elif len(temp) < len(ans):
                        ans = temp
                    elif len(temp) == len(ans) and temp < ans:
                        ans = temp
                    break
                elif count > k:
                    break
        return ans
