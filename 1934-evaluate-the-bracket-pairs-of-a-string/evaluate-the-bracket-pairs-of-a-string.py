class Solution:
    def evaluate(self, s, knowledge):
        values = {}
        # Store knowledge in dictionary
        for key, value in knowledge:
            values[key] = value
        result = []
        i = 0
        while i < len(s):
            # Start of bracket pair
            if s[i] == '(':
                i += 1
                key = []
                # Read key until ')'
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                key = ''.join(key)
                # Replace key with value
                if key in values:
                    result.append(values[key])
                else:
                    result.append('?')
                # Skip ')'
                i += 1
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)