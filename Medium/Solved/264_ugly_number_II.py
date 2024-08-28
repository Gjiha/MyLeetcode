
'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
'''


import heapq as h

'''
class Solution(object):


    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]

        h.heapify(heap)
      

        ugliest = 0
        i = 0

        while(i < n):
            p = h.heappop(heap)
            ugliest = p
            print(ugliest)
            print(heap)
            print(d)
            i += 1

            c = True

            if d.get(ugliest * 2) is None:
                d[ugliest * 2] = True
                heap.append(ugliest * 2)

            if d.get(ugliest * 3) is None:
                d[ugliest * 3] = True
                heap.append(ugliest * 3)

            if d.get(ugliest * 5) is None:
                d[ugliest * 5] = True
                heap.append(ugliest * 5)

            h.heapify(heap)
            
            
            

        return ugliest  

sol = Solution()
print(sol.nthUglyNumber(15))
'''


class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2,3,5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = h.heappop(uglyHeap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    h.heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)
        return curr
    




        
        