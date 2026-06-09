class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        minValue = min(nums)
        maxValue = max(nums)
        return (maxValue - minValue) * k 