class Solution:
    def lexPalindromicPermutation(self, s, target):
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        odd_count = 0
        middle = ""
        for i in range(26):
            if count[i] % 2 == 1:
                odd_count += 1
                middle = chr(i + 97)
        if odd_count > 1:
            return ""
        half_count = [0] * 26
        for i in range(26):
            half_count[i] = count[i] // 2
        m = len(s) // 2
        prefix = target[:m]
        temp = half_count[:]
        possible = True
        for ch in prefix:
            x = ord(ch) - 97
            if temp[x] == 0:
                possible = False
                break
            temp[x] -= 1
        if possible:
            same_half = prefix
            candidate = same_half + middle + same_half[::-1]
            if candidate > target:
                return candidate
        for i in range(m - 1, -1, -1):
            temp = half_count[:]
            possible = True
            for j in range(i):
                x = ord(prefix[j]) - 97
                if temp[x] == 0:
                    possible = False
                    break
                temp[x] -= 1
            if not possible:
                continue
            current = ord(prefix[i]) - 97
            for c in range(current + 1, 26):
                if temp[c] > 0:
                    temp[c] -= 1
                    new_half = prefix[:i] + chr(c + 97)
                    for k in range(26):
                        new_half += chr(k + 97) * temp[k]
                    return new_half + middle + new_half[::-1]
        return ""
