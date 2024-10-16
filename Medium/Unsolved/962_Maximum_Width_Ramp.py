class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        listOftried = []
        i = 0
        j = len(nums) - 1
        returnValue = 0
        appoggio = []

        while i < len(nums) and i < j:
            if nums[i] > nums[j]:
                listOftried.append(nums[i])
                i += 1
            else:
                if returnValue <= j - i:
                    returnValue = j - i 
                j -= 1 
                
        
        return returnValue
    
sol = Solution()
print(sol.maxWidthRamp([6,0,8,2,1,5]))


            

        