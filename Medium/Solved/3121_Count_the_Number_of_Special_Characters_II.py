class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dictOfLower = dict()
        dictOfUpper = dict()

        for i, char in enumerate(word):
            if ord('A') <= ord(char) <= ord('Z'):
                if char not in dictOfUpper:
                    dictOfUpper[char] = i
            else:
                if char not in dictOfLower:
                    dictOfLower[char] = i 
                else:
                    dictOfLower[char] = i        

        results = 0
        for char in dictOfLower.keys():
            lastPos = dictOfLower[char]
            if char.upper() in dictOfUpper and lastPos < dictOfUpper[char.upper()]:
                results += 1
        
        return results
            
                
