import pprint

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        Graph = {}
        
        for (start, end) in edges:

            if start not in Graph:
                Graph[start] = {}

            if end not in Graph:
                Graph[end] = {}

            Graph[start][end] = 'ok'
            Graph[end][start] = 'ok'

            markedNodes = set()
        
        return self.dfs(source, destination, Graph, markedNodes)

    
    def dfs(self, nodo : int, destination : int, Graph : dict, markedNodes: set):
        if nodo == destination:
            return True
        
        for end in Graph[nodo].keys():

            if end not in markedNodes:
                markedNodes.add(end)
                if self.dfs(end,destination, Graph, markedNodes):
                    return True

        return False
        
        
    

    
sol = Solution()
pprint.pprint(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
