class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        output =  0
        for num in costs:
            if num > coins:
                return output
            else:
                output += 1
                coins -= num
        return output