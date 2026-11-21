class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)            
        new_parent = list(parent)
        last_seen = [-1] * 26
        stack = [(0, 0)]
        saved_prev = [-1] * n        
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - ord('a')
            if state == 0:
                if last_seen[c] != -1:
                    new_parent[u] = last_seen[c]
                saved_prev[u] = last_seen[c]
                last_seen[c] = u             
                stack.append((u, 1))
                for v in children[u]:
                    stack.append((v, 0))
            else:
                last_seen[c] = saved_prev[u]
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        answer = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in new_children[u]:
                stack.append(v)               
        for u in reversed(order):
            if new_parent[u] != -1:
                answer[new_parent[u]] += answer[u]               
        return answer