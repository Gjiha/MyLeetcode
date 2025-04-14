class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for number in range(low, high + 1):
            digits = str(number)
            n = len(digits)

            if n % 2 == 0:
                first = 0
                second = 0
                for i in range(n//2):
                    first += int(digits[i])
                    second += int(digits[i + n//2])
                if first == second:
                    count += 1
        
        return count
                


