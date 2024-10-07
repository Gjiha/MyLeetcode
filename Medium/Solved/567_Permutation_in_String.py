class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutationDict = {}
        for char in s1:
            if char not in permutationDict:
                permutationDict[char] = 1
            else:
                permutationDict[char] += 1

        controlDict = {}
        
        index = 0
        while index < len(s1) and index < len(s2):
            if s2[index] not in controlDict:
                controlDict[s2[index]] = 1
            else:
                controlDict[s2[index]] += 1
            index += 1
        
        if controlDict == permutationDict:
            return True
        
        while index < len(s2):

            controlDict[s2[index - len(s1)]] -= 1

            if controlDict[s2[index - len(s1)]] == 0:
                controlDict.pop(s2[index - len(s1)])
            
            if s2[index] not in controlDict:
                controlDict[s2[index]] = 1
            else:
                controlDict[s2[index]] += 1
            
            if controlDict == permutationDict:
                return True
            
            index += 1
        
        return False

sol = Solution()
a = "cdca"
b = "adc"
print(sol.checkInclusion(b,a))

