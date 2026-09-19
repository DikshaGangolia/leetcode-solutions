class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find closest point of rectangle to circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        # Calculate squared distance
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        distance_squared = dx * dx + dy * dy
        # Check if point lies inside or on circle
        return distance_squared <= radius * radius