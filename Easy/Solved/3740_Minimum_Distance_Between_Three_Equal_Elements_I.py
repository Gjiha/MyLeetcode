class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        dictOfNums = {}
        for num, i in enumerate(nums):
            if num in dictOfNums:
                dictOfNums[num].append(i)
            else:
                dictOfNums[num] = [i]
        
        for num in dictOfNums:
            result = float('inf')
            m = len(num)
            if m >= 3:
                i = 3
                while i < m:
                    "caio"