class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        # Rows without reservations can have 2 groups
        answer = (n - len(rows)) * 2

        # Check rows having reservations
        for seats in rows.values():

            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats

            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats

            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats

            if left and right:
                # Can place two groups: 2-5 and 6-9
                answer += 2

            elif left or middle or right:
                # Can place one group
                answer += 1

        return answer