import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """

class Tree(object):

    def __init__(self, root: str, edges: list[tuple[str]], weight: list[tuple]) -> None:

        self.tree = {}
        self.root = root
        self.nodes = set()
        
        self.nodes.add(root)

        for i, (start, end) in enumerate(edges):

            if start not in self.tree:
                self.tree[start] = {'child': None}
                self.nodes.add(start)
            
            if end not in self.tree:
                self.tree[end] = {'child': None, 'father': start}
                self.nodes.add(end)
            
            self.tree[start][end] = weight[i]

            if self.tree[start]['child'] == None:
                self.tree[start]['child'] = set()
                self.tree[start]['child'].add(end)
            else:
                self.tree[start]['child'].add(end)

            self.tree[end]['father'] = start
    
    def __str__(self) -> None:

        return f"Tree : {self.tree}\nRoot : {self.root}\nNodes : {self.nodes}"
    
    def addEdge(self, edge: tuple[str], weight: float) -> None:
        '''aggiunta di un arco all'albero'''
        
        start, end = edge

        if start not in self.tree:
            self.tree[start] = {'child': None}
            self.nodes.add(start)
        
        if end not in self.tree:
            self.tree[end] = {'child': None, 'father': start}
            self.nodes.add(end)
        
        self.tree[start][end] = weight

        if self.tree[start]['child'] == None:
            self.tree[start]['child'] = set()
            self.tree[start]['child'].add(end)
        else:
            self.tree[start]['child'].add(end)

        self.tree[end]['father'] = start

    def addEdgesFrom(self, listOfEdges: list[tuple[str]], listOfWeight: list[float]) -> None:
        '''aggiunta di archi all'albero a partire da una lista'''

        for i ,(start, end) in enumerate(listOfEdges):

            self.addEdge((start, end), listOfWeight[i])
    
    def removeNode(self, node: str) -> None:
        '''rimozione di un ramo dell'albero a partire da un nodo'''

        listToRemove = self.dfs(node)

        if self.tree[node]['child'] != None:
            for descendants in listToRemove:
                self.tree.pop(descendants)
                self.nodes.remove(descendants)
        
        father = self.tree[node]['father']
        self.tree.pop(node)
        self.tree[father].pop(node)
        self.tree[father]['child'].remove(node)
        self.nodes.remove(node)

    

    def dfs(self, nodo: str, listOfNodeVisited = []) -> list[str]:
        '''esecuzione di una dfs a partire dal nodo indicato'''

        if self.tree[nodo]['child'] == None:
            return listOfNodeVisited

        for i in self.tree[nodo]['child']:
            listOfNodeVisited.append(i)
            self.dfs(i, listOfNodeVisited)
        
        return listOfNodeVisited
            

        

    
            


        
        


class Graph(object):

    def __init__(self, edges: list[tuple[str]], weight: list[float]):

        self.graph = {}
        self.nodes = set()

        for i, (start, end) in enumerate(edges):

            if start not in self.graph:
                self.graph[start] = {}
                self.nodes.add(start)

            if end not in self.nodes:
                self.nodes.add(end)

            self.graph[start][end] = weight[i]
    
    def __str__(self) -> str:

        return f"Graph: {self.graph}\nNodes: {self.nodes}"
    
    def addNode(self, newNode : str):  #aggiunta di un nodo
        '''aggiunta di nodo al grafo'''

        self.graph[newNode] = {}
        self.nodes.add(newNode)

    def addNodesFrom(self, newNodes : list[str]) -> None:  
        '''aggiunta di nodi al grafo a partire da una lista'''

        for i in newNodes:

            self.graph[i] = {}
            self.nodes.add(i)    
    
    def addEdge(self, newEdge : tuple, newWeight : float) -> None:  
        '''aggiunta di un arco al grafo'''

        if newEdge[0] not in self.graph:
            self.graph[newEdge[0]] = {}
        
        if newEdge[0] not in self.nodes:
            self.nodes.add(newEdge[0])

        if newEdge[1] not in self.nodes:
            self.nodes.add(newEdge[1])

        self.graph[newEdge[0]][newEdge[1]] = newWeight


    def addEdgesFrom(self, newEdges : list[tuple[str]], newWeights : list[float]) -> None:  
        '''aggiunta di una lista di archi al grafo'''

        for i, (start, end) in enumerate(newEdges):

            if start not in self.graph:
                self.graph[start] = {}
            
            if start not in self.nodes:
                self.nodes.add(start)

            if end not in self.nodes:
                self.nodes.add(end)

            self.graph[start][end] = newWeights[i]        
    
    def removeNode(self, nodeToRemove: str) -> None:  
        '''rimozione di un nodo dal grafo'''

        self.graph.pop(nodeToRemove)
        self.nodes.remove(nodeToRemove)


    def removeNodesFrom(self, nodesToRemove: list[str]) -> None: 
        '''rimozione di una lista di nodi dal grafo'''

        for i in nodesToRemove:
            self.removeNode(i)
    
    def removeEdge(self, edgeToRemove: tuple[str]) -> None:
        '''rimozione di un arco dal grafo'''

        start, end = edgeToRemove
        self.graph[start].pop(end)
    
    def removeEdgesFrom(self, edgesToRemove : list[tuple[str]]) -> None:
        '''rimozione di archi dal grafo a partire da una lista'''

        for i in edgesToRemove:
            self.removeEdge(i)


def Djkstra(grafo: Graph, start: str, end: str) -> Tree:
    '''dato un grafo con pesi >= 0 ritorna un albero con i cammini minimi'''

    priority = heapq.PriorityQueue()

    secureNode = set()


    







e = [['a','b'], ['b', 'c'], ['c', 'd']]
w = [0,1,2]

albero = Tree('a', e, w)
albero.addEdgesFrom([('a', 'f'), ('a', 'g')], [4, 8])
print(albero)
print('\n')
albero.removeNode('b')
print(albero)

#grafo = Graph(e, w)
#grafo.removeEdge(('c', 'd'))
#print('\n', grafo)
