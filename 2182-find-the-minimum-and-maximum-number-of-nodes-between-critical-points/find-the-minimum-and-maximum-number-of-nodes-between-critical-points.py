class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        pos = 1
        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            nextNode = curr.next

            # Check local maximum or local minimum
            if ((curr.val > prev.val and curr.val > nextNode.val) or
                (curr.val < prev.val and curr.val < nextNode.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    minDist = min(minDist, pos - last)

                last = pos

            prev = curr
            curr = nextNode
            pos += 1

        # Less than 2 critical points
        if first == last:
            return [-1, -1]

        maxDist = last - first

        return [minDist, maxDist]