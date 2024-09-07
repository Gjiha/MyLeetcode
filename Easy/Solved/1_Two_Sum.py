class Solution:
    def binarySearch(self, list: list, start: int, end: int, key: int):
        medium = (start + end) // 2
        if list[medium] == key:
            return True
        if start > end:
            return False
        if list[medium] > key:
            return  self.binarySearch(list, start, medium - 1, key)
        elif list[medium] < key:
            return  self.binarySearch(list, medium + 1, end, key)
        
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sortedNums = sorted(nums)
        listToReturn = []
        for i in range(len(nums)):
            restForTarget = target - nums[i]
            if self.binarySearch(sortedNums, 0, len(sortedNums) - 1, restForTarget):
                for j in range(len(nums)):
                    if nums[j] == restForTarget and j != i:
                        listToReturn.append(i)
                        listToReturn.append(j)
                        return listToReturn
                
        return listToReturn
    
sol = Solution()
print(sol.twoSum([3,2,4], 6))