class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        if len(sentence1) > len(sentence2):
            listToObtain = sentence1
            listToComplete = sentence2
        else:
            listToComplete = sentence1
            listToObtain = sentence2
        
        i = 0
        j = 1
        startingList = []
        endingList = []

        while i <= len(listToComplete) - j:
            if listToComplete[i] == listToObtain[i]:
                startingList.append(listToComplete[i])
                i += 1
            
            elif listToComplete[len(listToComplete) - j] == listToObtain[len(listToObtain) - j]:
                endingList.append(listToComplete[len(listToComplete) - j])
                j += 1

            else:
                break

        endingList.reverse()
        
        controlList = startingList[:] + endingList[:]

        if controlList != listToComplete:
            return False
        
        while i <= len(listToObtain) - j:
            startingList.append(listToObtain[i])
            i += 1
        
        startingList.extend(endingList)
            
        return True if listToObtain == startingList else False
    

x = "My name is Hailey"
y = "My Hailey"
sol = Solution()
print(sol.areSentencesSimilar(x,y))
