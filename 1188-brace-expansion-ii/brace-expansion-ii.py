class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            result = set()
            current = {""}
            while i < len(expression) and expression[i] != '}':
                # Case 1: comma
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                # Case 2: opening brace
                elif expression[i] == '{':
                    sub_result, i = parse(i + 1)
                    # Concatenate current with sub_result
                    new_current = set()
                    for a in current:
                        for b in sub_result:
                            new_current.add(a + b)
                    current = new_current
                # Case 3: lowercase letter
                else:
                    ch = expression[i]
                    new_current = set()
                    for word in current:
                        new_current.add(word + ch)
                    current = new_current
                    i += 1
            result |= current
            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1
            return result, i
        result, _ = parse(0)
        return sorted(result)