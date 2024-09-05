class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        sumOfM = sum(rolls)
        sumOfN = (mean * (n + m)) - sumOfM
        intNValue = sumOfN // n
        floatNValue = sumOfN / n
        print("sumOfM: ", sumOfM)
        print("sumOfN: ", sumOfN)
        print("intNValue: ", intNValue)
        print("floatNValue: ", floatNValue)

        listToReturn = []
        if floatNValue > 6 or floatNValue < 1:
            return listToReturn
        elif floatNValue > intNValue:

            listToReturn = [intNValue] * n

            intTotal = intNValue * n
            intRemain = sumOfN - intTotal
            i = 0
            while intRemain > 0:
                if listToReturn[i] < 6:
                    intRemain -= 1
                    listToReturn[i] += 1
                i += 1
        else:
            listToReturn = [intNValue] * n

        
        return listToReturn
        
sol = Solution()
print(sol.missingRolls([3,2,4,3], 4, 2))