class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        leftSum = [0]
        rightSum = [0]
        n =len(nums)
        for i in range(n):
            leftSum.append(leftSum[i] + nums[i])
            rightSum.append(rightSum[i] + nums[n-1-i])

        returnList = []
        for i in range(n):
            returnList.append(abs(leftSum[i] - rightSum[n-1-i]))
        
        return returnList




