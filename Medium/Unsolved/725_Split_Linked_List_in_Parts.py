# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"[val: {self.val}, next: {self.next}]"

class Solution:
    def splitListToParts(self, head, k: int):
        node = head
        lenght = 0

        while(node != None):
            lenght += 1
            node = node.next
        
        #print(lenght)
        
        originalNode = head
        newList = ListNode()
        nodeToReturn = newList

        valInList = lenght // k

        for _ in range(k):

            newList.next = ListNode()
            newNode = ListNode(originalNode.val)
            newHead = newNode
            originalNode = originalNode.next

            for _ in range(valInList - 1):
                newNode.val = originalNode.val
                newNode.next = ListNode()
                newNode = newNode.next
                originalNode = originalNode.next

            newList.val = newHead
            newList = newList.next

        return nodeToReturn


    
head = ListNode( 1,  ListNode( 2,  ListNode( 3,  None)))

sol = Solution()
print(sol.splitListToParts(head, 3))

n = ListNode(5, ListNode(7))
n = n.next
print(n)
