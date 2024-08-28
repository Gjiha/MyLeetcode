'''
You are given a 0-indexed integer array nums having length n.

You are allowed to perform a special move any number of times (including zero) on nums. In one special move you perform the 
following steps in order:

    Choose an index i in the range [0, n - 1], and a positive integer x.
    Add |nums[i] - x| to the total cost.
    Change the value of nums[i] to x.

A palindromic number is a positive integer that remains the same when its digits are reversed. For example, 121, 2552
and 65756 are palindromic numbers whereas 24, 46, 235 are not palindromic numbers.

An array is considered equalindromic if all the elements in the array are equal to an integer y, where y is a palindromic
number less than 109.

Return an integer denoting the minimum possible total cost to make nums equalindromic by performing any number of special moves.
'''
import pprint as pp

class Solution(object):

#    def generatePalindomeNumber(self, min: int, max:int):
#        listToReturn = []
#        number = minimo
#        while number <= massimo:
#            string = str(number)
#            i = 0
#            j = len(string) - 1
#            palindrome = False
#            while(i <= j):
#                if string[i] != string[j]:
#                    palindrome = False
#                    break
#                i += 1
#                j -= 1
#                palindrome = True
#            if palindrome:
#                listToReturn.append(number)
#            number += 1
#
#        return listToReturn
#
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        
        minimo = min(nums)
        if(minimo >= 100):
            minimo -= 100
        massimo = max(nums) + 100

        listOfEqualindromic = []
        number = minimo
        while number <= massimo:
            string = str(number)
            if string == string[::-1]:
                listOfEqualindromic.append(number)
            number += 1

        

        OPT = [[0] * len(listOfEqualindromic) for _ in range(n)]

        w = 0

        listToReturn = []

        minim = float('inf')
        indexToReturn = 0

        for i in range(len(listOfEqualindromic)):
            sum = 0
            for j in range(n):   
                w = abs(nums[j] - listOfEqualindromic[i])             
                OPT[j][i] = w
                sum += w

            if(sum < minim):
                minim = sum
                #print(listOfEqualindromic[i])
        
        return minim



        
sol = Solution()
pp.pprint(sol.minimumCost([1,2,3,4,5]))