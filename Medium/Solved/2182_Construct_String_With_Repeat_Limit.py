class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        dictOfChar = {}

        for char in s:
            if char not in dictOfChar:
                dictOfChar[char] = 1
            else:
                dictOfChar[char] += 1
        
        listOfChar = list(dictOfChar.keys())
        listOfChar = sorted(listOfChar)

        stringToReturn = ''

        term = False

        i = len(listOfChar) - 1

        while len(s) > len(stringToReturn):
            j = 0
            
            while j < repeatLimit:
                
                if dictOfChar[listOfChar[i]] > repeatLimit:

                    stringToReturn += listOfChar[i]*repeatLimit
                    dictOfChar[listOfChar[i]] -= repeatLimit
                    break

                elif dictOfChar[listOfChar[i]] > 0:
                    
                    stringToReturn += listOfChar[i]
                    dictOfChar[listOfChar[i]] -= 1
                    j += 1
                
                else:
                    break

            if dictOfChar[listOfChar[i]] > 0 and i > 0:
                t = i - 1
                term = True
                while t >= 0:
                    if dictOfChar[listOfChar[t]] > 0:
                        term = False 
                        stringToReturn += listOfChar[t]
                        dictOfChar[listOfChar[t]] -= 1
                        break
                    t -= 1

            if (dictOfChar[listOfChar[i]] > 0 and i == 0) or (term == True):
                break
            
            if dictOfChar[listOfChar[i]] == 0:
                dictOfChar.pop(listOfChar[i])
                listOfChar.pop()
                i -= 1

            
            

        return stringToReturn
                    

         


    
sol = Solution()
print(sol.repeatLimitedString("aababab",2))