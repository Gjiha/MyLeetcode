class Solution:
    def binary(self, arr, start, end, value, setOfVisited):
        if start > end:
            return -1
        
        medium = start + (end - start)//2

        if arr[medium] == value and medium not in setOfVisited:
            return medium
        elif arr[medium] <= value:
            return self.binary(arr, medium + 1, end, value, setOfVisited)
        else:
            return self.binary(arr, start, medium - 1, value, setOfVisited)

    def canArrange(self, arr: list[int], k: int) -> bool:

        arr.sort()
        visitedNumber = set()
        find = 0
        index = 0
        n = len(arr)// 2

        while find < n:
            result = 1
            paired = False

            while not paired:
                valueToSearch = (result * k) - arr[index]
                indexFinded = self.binary(arr, 0, len(arr) - 1, valueToSearch, visitedNumber)
                print("valueToSearch: ", valueToSearch)
                
                if indexFinded != -1:
                    paired = True
                    print(f"({index}, {indexFinded})")
                    visitedNumber.add(index)
                    visitedNumber.add(indexFinded)
                result += 1
            
            if paired == False:
                return paired
            
            find += 1
            index += 1

        return True


sol = Solution()
arr = [1,2,3,4,5,6]
k = 7

print(sol.canArrange(arr, k))

