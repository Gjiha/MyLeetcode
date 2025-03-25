class Solution:
    def minOperations(self, nums: list[int]) -> int:

        moves = 0

        for i in range(len(nums)-2):

            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
    
                moves += 1
            
        
        if nums[-1] and nums[-2]:
            return moves
        
        return -1
    
sol = Solution()
sol.minOperations([0,1,1,1,0,0])

        



         