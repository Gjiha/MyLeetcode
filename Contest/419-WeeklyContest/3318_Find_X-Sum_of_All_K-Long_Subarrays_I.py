import heapq as hq

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        window = {}

        for i in range(k):
            if nums[i] not in window:
                window[nums[i]] = 1
            else:
                window[nums[i]] += 1
        
        listOfSums = []
        listOfOccurrences = []

        for item in window:
            listOfOccurrences.sort(key=lambda x: x[1], reverse=True)

        i = 0
        intToSum = 0

        while i < x and i < len(listOfOccurrences):
            intToSum += listOfOccurrences[i][0] * listOfOccurrences[i][0]

        listOfSums.append(intToSum)

        while i < len(nums):
            listOfOccurrences = []
            
            if nums[i] not in window:
                window[nums[i]] = 1
            else:
                window[nums[i]] += 1
            
            window[nums[k - i]] -= 1
            if window[nums[k - i]] == 0:
                window.pop(nums[k - i])
            
            listOfOccurrences.extend(window.items())
            listOfOccurrences.sort(key=lambda x: x[1], reverse=True)

            i = 0
            intToSum = 0

            while i < x and i < len(listOfOccurrences):
                intToSum += listOfOccurrences[i][0] * listOfOccurrences[i][0]

            listOfSums.append(intToSum)

            i += 1
        
        return listOfSums
            
            

