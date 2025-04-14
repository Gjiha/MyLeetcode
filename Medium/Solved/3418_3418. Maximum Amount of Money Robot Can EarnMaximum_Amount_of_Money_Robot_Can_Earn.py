import pprint as pp

class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        
        n = len(coins)
        m = len(coins[0])
        opt = [[[0,0,0] for _ in range(m)] for _ in range(n)]


        opt[0][0] = [coins[0][0],0,0]

        for i in range(1,n):
            opt[i][0][0] = opt[i-1][0][0] + coins[i][0]
            opt[i][0][1] = max(opt[i-1][0][0], opt[i-1][0][1] + coins[i][0])
            opt[i][0][2] = max(opt[i-1][0][1], opt[i-1][0][2] + coins[i][0])
        
        for j in range(1,m):
            opt[0][j][0] = opt[0][j-1][0] + coins[0][j]
            opt[0][j][1] = max(opt[0][j-1][0], opt[0][j-1][1] + coins[0][j])
            opt[0][j][2] = max(opt[0][j-1][1], opt[0][j-1][2] + coins[0][j])

        for i in range(1,n):
            for j in range(1,m):
                opt[i][j][0] = max(opt[i-1][j][0], opt[i][j-1][0]) + coins[i][j]
                opt[i][j][1] = max( max(opt[i-1][j][0], opt[i][j-1][0]), max(opt[i-1][j][1], opt[i][j-1][1]) + coins[i][j])
                opt[i][j][2] = max( max(opt[i-1][j][1], opt[i][j-1][1]), max(opt[i-1][j][2], opt[i][j-1][2]) + coins[i][j])
        
        return max(opt[n-1][m-1])


sol = Solution()
print(sol.maximumAmount([[1,2,3],[1,3,3],[1,2,3],[1,2,3]]))