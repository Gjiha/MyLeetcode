class Solution:
    def isHappy(self, n: int) -> bool:
        
        visitedNumber = set()
        happy = n

        while(happy != 1):
            string = str(happy)
            happy = 0
            for digit in string:
                happy += int(digit)**2

            print(happy)

            if happy == 1:
                return True
            elif happy in visitedNumber:
                return False
            else:
                visitedNumber.add(happy)
        
        return True

sol = Solution()
print(sol.isHappy(19))
