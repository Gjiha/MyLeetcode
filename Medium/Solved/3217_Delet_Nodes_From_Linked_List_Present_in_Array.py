
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head):
        
        numToDelete = set()
        for num in nums:
            if num not in numToDelete:
                numToDelete.add(num)
        
        while head.next != None and head.val in numToDelete:
            head = head.next
            

        node = head
        
        while node is not None and node.next is not None:
            if node.next.val in numToDelete:
                node.next = node.next.next
            else:
                node = node.next
        
        return head
            

