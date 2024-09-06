# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head):
        
        numToDelete = set()
        for num in nums:
            if num not in numToDelete:
                numToDelete.add(num)
        
        
        