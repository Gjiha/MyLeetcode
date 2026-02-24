class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root) -> int:
        return self.recursiveSum(root,0)

    def recursiveSum(self, node, sum):
        if node == None: 
            return 0

        value = sum * 2 + node.val

        if(node.left == None and node.right == None ):
            return  value 

        leftSum = self.recursiveSum(node.left, value )
        rightSum = self.recursiveSum(node.right, value )

        return leftSum + rightSum
        