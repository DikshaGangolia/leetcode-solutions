class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        queue = [s]
        visited = {s}
        while queue:
            next_queue = []
            for current in queue:
                if isValid(current):
                    results = []
                    for item in queue:
                        if isValid(item):
                            results.append(item)
                    return results
                for i in range(len(current)):
                    if current[i] not in '()':
                        continue
                    new_string = current[:i] + current[i + 1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)
            queue = next_queue
        return [""]