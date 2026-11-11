class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2
        elif need2 > need1:
            return need1 * costBoth + (need2 - need1) * min(cost2, costBoth)
        else:
            return need2 * costBoth + (need1 - need2) * min(cost1, costBoth)
