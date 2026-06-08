class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        prevNums = []
        midNums = []
        lastNums = []
        for num in nums:
            if num < pivot:
                prevNums.append(num)
            elif num == pivot:
                midNums.append(num)
            else:
                lastNums.append(num)
        
        prevNums.extend(midNums)
        prevNums.extend(lastNums)

        return prevNums