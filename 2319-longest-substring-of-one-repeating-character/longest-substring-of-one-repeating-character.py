class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            left_char = a[0]
            right_char = b[1]
            length = a[2] + b[2]
            prefix = a[3]
            suffix = b[4]
            best = max(a[5], b[5])
            if a[1] == b[0]:
                best = max(best, a[4] + b[3])
                # Entire left segment has same character
                if a[3] == a[2]:
                    prefix = a[2] + b[3]
                # Entire right segment has same character
                if b[4] == b[2]:
                    suffix = a[4] + b[2]
            return [
                left_char,
                right_char,
                length,
                prefix,
                suffix,
                best
            ]
        def build(node, left, right):
            if left == right:
                tree[node] = [
                    s[left],   # left character
                    s[left],   # right character
                    1,         # length
                    1,         # prefix
                    1,         # suffix
                    1          # best
                ]
                return
            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def update(node, left, right, index, char):
            if left == right:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return
            mid = (left + right) // 2
            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        build(1, 0, n - 1)
        answer = []
        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][5])
        return answer