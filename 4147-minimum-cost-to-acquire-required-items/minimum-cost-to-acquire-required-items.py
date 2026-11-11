class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2
        common = min(need1, need2)
        total_cost = common * costBoth
        if need1 > need2:
            rem = need1 - common
            total_cost += rem * min(cost1, costBoth)
        elif need2 > need1:
            rem = need2 - common
            total_cost += rem * min(cost2, costBoth)
        return total_cost