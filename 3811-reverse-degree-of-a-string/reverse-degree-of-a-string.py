class Solution:
    def reverseDegree(self, s):
        answer = 0
        for i in range(len(s)):
            reverse_position = 26 - (ord(s[i]) - ord('a'))
            string_position = i + 1
            answer += reverse_position * string_position
        return answer