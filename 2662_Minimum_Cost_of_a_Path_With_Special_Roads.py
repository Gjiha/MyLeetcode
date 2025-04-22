import pprint as pp
import heapq as hq

class Solution:
    def createGraph(self, targetStart: list[int], targetEnd: list[int], specialRoads: list[list[int]]) -> None:
        
        graph = {tuple(targetStart):{}}
        graph[tuple(targetStart)][tuple(targetEnd)] = abs(targetStart[0] - targetEnd[0]) + abs(targetStart[1] - targetEnd[1])

        for startX, startY, endX, endY, weight in specialRoads:

            graph[tuple(targetStart)][(startX,startY)] = abs(targetStart[0] - startX) + abs(targetStart[1] - startY)

            graph[(startX,startY)] = {}
            graph[(startX,startY)][(endX, endY)] = weight

            graph[(endX,endY)] = {}
            graph[(endX,endY)][tuple(targetEnd)] = abs(targetEnd[0] - endX) + abs(targetEnd[1] - endY)

            for newStartX, newStartY, newEndX, newEndY, _ in specialRoads:
                if newEndX != endX and newEndY != endY:
                    graph[(endX,endY)][(newStartX, newEndX)] = abs(newStartX - endX) + abs(newStartY - endY)
        
        self.graph = graph
        return
    
    def dijkstra(start, end) -> int:

        pass
    
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        pass


sol = Solution()
sol.createGraph([1,1], [4,5], [[1,2,3,3,2],[3,4,4,5,1]])