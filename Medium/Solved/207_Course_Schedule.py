class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        dictOfCourses = {}

        if len(prerequisites) == 0:
            return True

        for edge in prerequisites:

            if edge[1] not in dictOfCourses:
                dictOfCourses[edge[1]] = {'in' : set(), 'out' : set()}
            
            dictOfCourses[edge[1]]['out'].add(edge[0])
            
            if edge[0] not in dictOfCourses:
                dictOfCourses[edge[0]] = {'in' : set(), 'out' : set()}
            
            dictOfCourses[edge[0]]['in'].add(edge[1])

        listWithoutIn = list(dictOfCourses.keys())
        listWithoutIn.sort(key=lambda x:len(dictOfCourses[x]['in']), reverse=True)
        print(listWithoutIn)
        print(dictOfCourses)

        nodeToExtract = listWithoutIn[-1] if len(dictOfCourses[listWithoutIn[-1]]['in']) == 0 else None

        print(nodeToExtract)

        while nodeToExtract != None:

            listToRemove = list(dictOfCourses[nodeToExtract]['out'])
            dictOfCourses.pop(nodeToExtract)

            for nodeOut in listToRemove:
                dictOfCourses[nodeOut]['in'].remove(nodeToExtract)
            
            listWithoutIn.pop()
            listWithoutIn.sort(key=lambda x:len(dictOfCourses[x]['in']), reverse=True)
            
            if len(listWithoutIn) == 0:
                return True
            else:
                nodeToExtract = listWithoutIn[-1] if len(dictOfCourses[listWithoutIn[-1]]['in']) == 0 else None

        return False
    



        

sol = Solution()
print(sol.canFinish(3,[[1,0],[2,1]]))



