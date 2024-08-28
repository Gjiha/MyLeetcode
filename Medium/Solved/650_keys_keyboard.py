class Solution(object):

    def scomposizione(n):
        i = 2
        fattori = []

        while(i * i <= n):
            if(n % i != 0):
                i += 1
            else:
                n = n // i
                fattori.append(i)
        if(n > 1):
            fattori.append(n)

        return sum(fattori)

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        moves = 0
        while(n != 0):
            if (n == 1):
                return moves
            elif(n % 2 == 0):
                moves += 2
                n = n // 2
            elif(n % 3 == 0):
                moves += 3
                n = n//3
            elif(n % 5 == 0):
                moves += 5
                n = n//5
            elif(n % 5 == 0):
                moves += 5
                n = n//5
            elif(n % 7 == 0):
                moves += 7
                n = n//7
            else:

                return moves + self.scomposizione(n)

#sol = Solution()
#print(sol.minSteps(741))




        


