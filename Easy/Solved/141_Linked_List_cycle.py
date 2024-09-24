# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        while head != None:
            if head.val == 'True':
                return True
            head.val = 'True'
            head = head.next
        return False
        
x = ListNode(1)
sol = Solution()
print(sol.hasCycle(x))