class Solution(object):

    def similNumbers(self, a: int, b: int) -> None:

        if a == b:
            return 1

        firstString = str(a)
        secondString = str(b)

        firstLen = len(firstString)
        secondLen = len(secondString)

        if(secondLen > firstLen):
            diff = secondLen - firstLen
            firstString = ('0'*diff) + firstString
            firstLen = len(firstString)

        elif(firstLen > secondLen):
            diff = firstLen - secondLen
            secondString = ('0'*diff) + secondString
            secondLen = len(secondString)



        wrongCounter = 0
        firstWrong = ''
        secondWrong = ''

        for i in range(firstLen):
        
            if firstString[i] != secondString[i] and wrongCounter == 0:

                wrongCounter += 1
                firstWrong = firstString[i]
                secondWrong = secondString[i]

            elif firstString[i] != secondString[i] and wrongCounter == 1:
               wrongCounter += 1

               if (firstWrong != secondString[i]) or (secondWrong != firstString[i]):
                    return 0

            elif firstString[i] != secondString[i] and wrongCounter > 1:
               return 0


        if wrongCounter < 2:
            return 0
        return 1

    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        simil = 0

        for i in range(n):
            for j in range(i + 1, n):

                x = 0
                
                x = self.similNumbers(nums[i], nums[j])

                simil +=  x
                if x == 1:
                    print(f"{simil} : nums[{i}] = {nums[i]}, nums[{j}] = {nums[j]}")
        
        return simil
    
    


sol = Solution()
print(sol.countPairs([50701, 751]))
                
            


                
