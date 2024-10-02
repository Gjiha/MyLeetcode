from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"[val: {self.val}, next: {self.next}]"
    
class Solution:

    def scorriLista(self, head: ListNode):
        node = head 
        repeat = True
        while node and node.next:
            if node.val == node.next.val:
                node = node.next
            else:
                return node.next
        return None

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = head
        while head and head.next:
            if head.val == head.next.val:
                newList = self.scorriLista(head)
                head = newList
            else:
                break
        
        returnValue = newList

        if returnValue == None:
            return returnValue
        
        head = newList.next

        while head and head.next:
            if head.val == head.next.val:
                newList.next = self.scorriLista(head)
                head = newList.next
            else:
                newList = head
                head = head.next
        
        return returnValue

x = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(5))))))))
sol = Solution()
print(sol.deleteDuplicates(x))