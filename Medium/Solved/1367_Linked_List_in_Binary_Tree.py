class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root, node) -> bool:
        if node is None:  
            return True
        
        if root is None:  
            return False
        
        
        if root.val == node.val:
            
            return self.dfs(root.left, node.next) or self.dfs(root.right, node.next)
        
        return False

    def isSubPath(self, head, root) -> bool:
        if root is None:
            return False
        
        return self.dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
