class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        listOfWords = sentence.split()
        n = len(listOfWords)

        if listOfWords[0][0] != listOfWords[-1][-1]:
            return False
        
        for i in range(n - 1):
            if listOfWords[i][-1] != listOfWords[i+1][0]:
                return False
            
        return True


