from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return Node
        
        coda = deque(node)
        dictOfNode = {node.val: Node(node.val, [])}

        while coda:
            cur = coda.popleft()
            clone = dictOfNode[cur.val]

            for nb in cur.neighbors:
                if nb.val not in dictOfNode:
                    dictOfNode[nb.val] = Node(nb.val , [])
                    coda.append(nb)

                clone.neighbors.append(dictOfNode[nb.val])
        
        return dictOfNode[node.val]

        

sol = Solution()
print(sol.cloneGraph([[2,4],[1,3],[2,4],[1,3]]))



