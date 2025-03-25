class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        maxLen = 1
        setOfNumber = None

        for number in nums:
            if not setOfNumber:
                setOfNumber = ListNode(number)
            else:
                index = 1

                p = setOfNumber
                if p.val & number:
                    setOfNumber = ListNode(number)
                else:
                    index += 1
                    q = p.next
                    while q!=None and p.next != None:
                        if q.val & number:
                            p.next = None
                        else:
                            p = p.next
                            q = q.next
                            index += 1

                    oldNode = setOfNumber
                    setOfNumber = ListNode(number, oldNode)

                    if index > maxLen:
                        maxLen = index

        return maxLen
                
sol = Solution()
x = sol.longestNiceSubarray([1,3,8,48,10])
print(x)
