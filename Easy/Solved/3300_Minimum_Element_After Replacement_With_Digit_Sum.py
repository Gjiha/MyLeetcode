class Solution:
    def minElement(self, nums: List[int]) -> int:
        results = []
        minValue = float('inf')
        for num in nums:
            value = 0
            for digit in str(num):
                value += int(digit)
            minValue = value if value < minValue else minValue
        return minValue
        