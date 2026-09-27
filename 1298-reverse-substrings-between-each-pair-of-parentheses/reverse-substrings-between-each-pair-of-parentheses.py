
class Solution:
    def reverseParentheses(self, s):
        stack = []
        for ch in s:
            if ch == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove '('
                stack.extend(temp)
            else:
                stack.append(ch)
        return ''.join(stack)