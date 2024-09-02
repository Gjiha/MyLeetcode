class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        
        totalChalk = sum(chalk)
        print(totalChalk)
        numberOfLap = k // totalChalk
        print(numberOfLap)
        remainingChalk = k -(totalChalk * numberOfLap)
        print(remainingChalk)

        i = -1
        while(remainingChalk >= 0):
            i += 1
            remainingChalk -= chalk[i]
        
        return i
    
sol = Solution()
print(sol.chalkReplacer([5,1,5], 22))
        