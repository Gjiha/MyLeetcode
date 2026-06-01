class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        n = len(cost)-1
        result = 0
        i = n
        while i >= 0:
            if i>=2:
                result += cost[i] + cost[i-1]
                i-=3
            elif i<=1:
                result += cost[i]
                i -= 1

        return result