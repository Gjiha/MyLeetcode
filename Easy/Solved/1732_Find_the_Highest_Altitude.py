class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newHeight = 0
        maxHeight = 0
        for num in gain:
            newHeight += num
            maxHeight = max(maxHeight, newHeight)
        return maxHeight