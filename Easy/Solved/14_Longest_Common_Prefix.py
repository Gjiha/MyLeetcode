class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key= lambda x: len(x))
        strToOut = ""
        strToCompare = strs[0]
        egual = True
        for i in range(len(strToCompare)):
            for str in strs:
                if strToCompare[i] != str[i]:
                    egual = False
                    break
            if egual == True:
                strToOut += strToCompare[i]
            else:
                return strToOut
        
        return strToOut

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))