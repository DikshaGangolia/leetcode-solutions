from collections import deque

class Solution:
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litters = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j
                elif classroom[i][j] == 'L':
                    litters.append((i, j))

        k = len(litters)

        litter_index = [[-1] * n for _ in range(m)]

        for index, (r, c) in enumerate(litters):
            litter_index[r][c] = index

        full_mask = (1 << k) - 1

        visited = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        queue = deque()
        queue.append((start_r, start_c, energy, 0))

        visited[start_r][start_c][0] = energy

        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while queue:

            size = len(queue)

            for _ in range(size):

                r, c, current_energy, mask = queue.popleft()

                if mask == full_mask:
                    return moves

                if current_energy == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = current_energy - 1
                    new_mask = mask

                    # Reset energy at R
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        index = litter_index[nr][nc]
                        new_mask |= (1 << index)

                    # Same state already reached with
                    # greater or equal energy
                    if visited[nr][nc][new_mask] >= new_energy:
                        continue

                    visited[nr][nc][new_mask] = new_energy
                    queue.append(
                        (nr, nc, new_energy, new_mask)
                    )

            moves += 1

        return -1