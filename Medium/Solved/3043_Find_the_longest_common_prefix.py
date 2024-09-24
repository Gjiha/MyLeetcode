import pprint as pp

class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:

        graph = {}
        originalGraph = graph

        for x in arr1:
            number = str(x)
            graph = originalGraph
            for digit in number:
                if digit not in graph:
                    graph[digit] = {}
                graph = graph[digit]

        returnValue = 0
        for y in arr2:
            tempMax = 0
            number = str(y)
            graph = originalGraph
            for digit in number:
                #print("digit: ", digit)
                if digit in graph:
                    tempMax += 1
                    graph = graph[digit]
                else:
                    break
            returnValue = max(returnValue, tempMax)
        
        return returnValue

        
sol = Solution()
print(sol.longestCommonPrefix([1,10,100],[1000]))

