class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        dictOfChar = {}

        for char in s:
            if char not in dictOfChar:
                dictOfChar[char] = 1
            else:
                dictOfChar[char] += 1
        
        listOfChar = list(dictOfChar.keys())
        listOfChar = sorted(listOfChar, reverse=True)

        stringToReturn = ''

        i = len(listOfChar) - 1

        while len(stringToReturn) != len(s):
            
            

        print(listOfChar)



    
sol = Solution()
print(sol.repeatLimitedString('mamzma',3))




