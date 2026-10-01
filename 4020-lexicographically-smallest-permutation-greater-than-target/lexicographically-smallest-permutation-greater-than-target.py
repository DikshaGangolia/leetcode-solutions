class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        for i in range(n - 1, -1, -1):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1
            possible = True
            for j in range(i):
                x = ord(target[j]) - 97
                if count[x] == 0:
                    possible = False
                    break
                count[x] -= 1
            if not possible:
                continue
            x = ord(target[i]) - 97
            for c in range(x + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    result = target[:i] + chr(c + 97)
                    for j in range(26):
                        result += chr(j + 97) * count[j]
                    return result
        return ""
