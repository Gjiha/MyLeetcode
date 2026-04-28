class Solution:

    # def executeQuery(self, query: list[int,int,int,int]):
    #     l,r,k,v = query

    #     idx = l
    #     while idx <= r:
    #         self.listOfInt[idx] = (self.listOfInt[idx] * v) % ((10**9) + 7)
    #         idx += k
    #     return 
    
    # def executeBitXor(self):
    #     result = 0
    #     for num in self.listOfInt:
    #         result ^= num
    #     return result

    # def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
    #     self.listOfInt = nums
    #     for query in queries:
    #         self.executeQuery(query)
        
    #     result = self.executeBitXor()

    #     return result

    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
            MOD = (10**9) + 7
            for query in queries:
                l,r,k,v = query

                idx = l
                for idx in range(l, r+1, k):
                    nums[idx] = (nums[idx] * v) % MOD

            result = 0
            for num in nums:
                result ^= num
            return result




