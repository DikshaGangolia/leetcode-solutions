class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        chars = list(s)
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                mask = 1 << (ord(chars[u]) - ord('a'))
                if p == -1:
                    prefix[u] = mask
                else:
                    depth[u] = depth[p] + 1
                    prefix[u] = prefix[p] ^ mask
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1
        LOG = n.bit_length()
        up = [parent[:]]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            j = 0
            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return parent[u]
        fenwick = [0] * (n + 2)
        def add(i, value):
            while i <= n + 1:
                fenwick[i] ^= value
                i += i & -i
        def query(i):
            result = 0
            while i > 0:
                result ^= fenwick[i]
                i -= i & -i
            return result
        def update_subtree(u, value):
            add(tin[u] + 1, value)
            add(tout[u] + 2, value)
        def get_mask(u):
            return prefix[u] ^ query(tin[u] + 1)
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))
                if old_bit != new_bit:
                    update_subtree(u, old_bit ^ new_bit)
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                mask = get_mask(u) ^ get_mask(v)
                mask ^= 1 << (ord(chars[w]) - ord('a'))
                answer.append((mask & (mask - 1)) == 0)
        return answer
