class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mirror(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.mirror(left.left, right.right) and self.mirror(left.right, right.left) 
        


    def isSymmetric(self, root) -> bool:
        if root == None: 
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False 
        return self.mirror(root.left, root.right)
        