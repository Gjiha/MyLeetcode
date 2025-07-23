import pprint as pp
import heapq as hq

class Solution:
    def createGraph(self, targetStart: list[int], targetEnd: list[int], specialRoads: list[list[int]]) -> None:

        targetStart = tuple(targetStart)
        targetEnd = tuple(targetEnd)
        graph = {targetStart:{targetEnd:abs(targetStart[0] - targetEnd[0]) + abs(targetStart[1] - targetEnd[1])}}

        starts = []

        for startX, startY, endX, endY, weight in specialRoads:
            start = (startX, startY)
            end = (endX, endY)

            starts.append(start)

            if start not in graph[targetStart] or graph[targetStart][start] > abs(targetStart[0] - start[0]) + abs(targetStart[1] - start[1]):
                graph[targetStart][start] = abs(targetStart[0] - start[0]) + abs(targetStart[1] - start[1])

            if start not in graph:
                graph[start] = {end: weight}
            elif end not in graph[start] or weight < graph[start][end]:
                graph[start][end] = weight
            if end not in graph:
                graph[end] = {targetEnd: abs(end[0] - targetEnd[0]) + abs(end[1] - targetEnd[1])}
            elif targetEnd not in graph[end] or abs(end[0] - targetEnd[0]) + abs(end[1] - targetEnd[1]) < graph[end][targetEnd]:
                graph[end][targetEnd] = abs(end[0] - targetEnd[0]) + abs(end[1] - targetEnd[1])
        
        for startX, startY, endX, endY, weight in specialRoads:
            start = (startX, startY)
            end = (endX, endY)

            for newStart in starts:
                if newStart != start:
                    if end not in graph:
                        graph[end] = {newStart: abs(end[0] - newStart[0]) + abs(end[1] - newStart[1])}
                    elif newStart not in graph[end] or abs(end[0] - newStart[0]) + abs(end[1] - newStart[1]) < graph[end][newStart]:
                        graph[end][newStart] = abs(end[0] - newStart[0]) + abs(end[1] - newStart[1])
            
        self.graph = graph
        pp.pprint(graph)
        return
    
    def dijkstra(self, start: tuple[int, int], target: tuple[int, int]) -> int:
        queue = [(0, start)]
        visited = set()
        distances = {start: 0}

        while queue:
            current_dist, current_node = hq.heappop(queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == target:
                return current_dist

            for neighbor, weight in self.graph.get(current_node, {}).items():
                distance = current_dist + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    hq.heappush(queue, (distance, neighbor))

        return float('inf')  # o None se preferisci indicare che non è raggiungibile

    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        self.createGraph(start, target, specialRoads)
        return self.dijkstra(tuple(start), tuple(target))


sol = Solution()
x = sol.minimumCost([1,1], [1,3], [[1,1,1,3,1],[1,2,1,1,2],[1,1,1,3,4],[1,3,1,2,5],[1,2,1,3,4]])
print(x)