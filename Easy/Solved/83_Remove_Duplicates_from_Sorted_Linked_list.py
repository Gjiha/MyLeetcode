# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):

        lastNumber = head

        while lastNumber != None and lastNumber.next != None:
            if lastNumber.val != lastNumber.next.val:
                lastNumber = lastNumber.next
            else:
                lastNumber.next = lastNumber.next.next
            

        return head