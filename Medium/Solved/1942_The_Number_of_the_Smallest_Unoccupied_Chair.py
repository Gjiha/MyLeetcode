import heapq as hq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        
        objective = times[targetFriend]
        arriveList = sorted(times, key=lambda x: x[0])
        leavingList = sorted(times, key=lambda x: x[1])

        prenotation = {}
        
        occupiedChair = 0 
        freeChair = []
      
        i = 0
        j = 0

        while i < len(arriveList):
            
            while j < len(leavingList) and leavingList[j][1] <= arriveList[i][0]:
                hq.heappush(freeChair, prenotation.pop(tuple(leavingList[j])))
                j += 1

            
            if not freeChair:
                prenotation[tuple(arriveList[i])] = occupiedChair
                occupiedChair += 1
            else:
                chair = hq.heappop(freeChair)
                prenotation[tuple(arriveList[i])] = chair

            
            if arriveList[i] == objective:
                return prenotation[tuple(objective)]

            i += 1
        
        return 

sol = Solution()
print(sol.smallestChair([[4,5],[12,13],[5,6],[1,2],[8,9],[9,10],[6,7],[3,4],[7,8],[13,14],[15,16],[14,15],[10,11],[11,12],[2,3],[16,17]],15))

        

        

