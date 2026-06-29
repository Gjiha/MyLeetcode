class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        value = 0
        for num in arr:
            if num > value :
                value += 1
        return value