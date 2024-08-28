class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1 : ListNode , l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        returnHead = ListNode(0)

        tail = returnHead
        carry = False

        while((l1 != None) and (l2 != None)):
            
            if(l1 != None):
                sum1 = l1.val
            else:
                sum1 = 0

            if(l2 != None):
                sum2 = l2.val
            else:
                sum2 = 0

            sum = sum1 + sum2

            if(carry):
                sum += 1
                carry = False

            if(sum >= 10):
                carry = True 
                sum -= 10

            newNode = ListNode(sum)
            tail.next = newNode
            tail = newNode

            if(l1.next != None):
                l1 = l1.next
            else:
                l1 = None

            if(l2.next != None):
                l2 = l2.next
            else:
                l2 = None
        print(returnHead)

sol = Solution()

l1 = ListNode(4)
l2 = ListNode(5)
print(sol.addTwoNumbers(l1,l2))
            
            


                           

            
            

        

        