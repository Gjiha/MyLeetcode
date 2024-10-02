class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        newList = set(arr)
        newList = list(newList)
        newList.sort()
        print(newList)

        dict = {}

        for i in range(len(newList)):
            if newList[i] not in dict:
                dict[newList[i]] = i
            
        print(dict)
        listToReturn = []
        for key in arr:
            listToReturn.append(dict[key] + 1)

        return listToReturn
        
sol = Solution()
x = [40,10,20,30]
print(sol.arrayRankTransform(x))