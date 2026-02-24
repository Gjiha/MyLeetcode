class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        j, i = 0, 0
        while i < n-1 and j < m:
            if strs[i][j] > strs[i+1][j]:
                j += 1
            else:
                i += 1
        
        return j

sol = Solution()
s = ["ca","bb","ac"]
print(sol.minDeletionSize(s))