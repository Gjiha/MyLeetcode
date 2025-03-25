# class ListNode:
#     def __init__(self, pos, lenght=1, next=None):
#         self.pos = pos
#         self.len = lenght
#         self.next = next
        
class Solution:

    # def createList(self, n: int) -> ListNode:
    #     Start = ListNode(None,0)

    #     p = Start

    #     for i in range(n):
    #         x = ListNode(i,1)

    #         p.next = x

    #         p = x
        
    #     return Start


        

    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        rectangles.sort()

        wightCouples = []        
        couple = []


        for i in rectangles:

            if not couple:
                couple = [i[0],i[2]]

            else:
                 
                if couple[0] <= i[0] and couple[1] >= i[2]:
                    continue

                elif couple[1] < i[2] and couple[1] > i[0]:
                        couple[1] = i[2]

                elif couple[1] <= i[0]:
                    wightCouples.append(couple[:])
                    couple = [i[0],i[2]]
        
        if not wightCouples:
            wightCouples.append(couple[:])
        elif wightCouples[-1][0] < couple[0]:
            wightCouples.append(couple[:])

        
        
        rectangles.sort(key= lambda x:x[1])

        heightCouples = []
        couple = []

        for i in rectangles:

            if not couple:
                couple = [i[1],i[3]]
            
            else:

                if couple[0] <= i[1] and couple[1] >= i[3]:
                    continue

                elif couple[1] < i[3] and couple[1] > i[1]:
                        couple[1] = i[3]

                elif couple[1] <= i[1]:
                    heightCouples.append(couple[:])
                    couple = [i[1],i[3]]
        
        if not heightCouples:
             heightCouples.append(couple[:])
        elif heightCouples[-1][0] < couple[0]:
            heightCouples.append(couple[:])

        
        if len(wightCouples) > 2 or len(heightCouples) > 2:
            return True
        
        return False


sol = Solution()
print(sol.checkValidCuts(3,[[0,0,1,3],[1,0,2,2],[2,0,3,2],[1,2,3,3]]))
