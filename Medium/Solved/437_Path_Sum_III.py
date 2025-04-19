# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        values = []
        count = self.dfsRic(root, targetSum, values)
        return count
    
    def dfsRic(self, node, targetSum, values):
        if node == None:
            return 0
        
        count = 0

        values = values[:]

        for i in range(len(values)):
            values[i] += node.val
            if values[i] == targetSum:
                count += 1

        if node.val == targetSum:
            count += 1

        values.append(node.val)
        print(values)

        count += self.dfsRic(node.left, targetSum, values)
        count += self.dfsRic(node.right, targetSum, values)
        

        return count
