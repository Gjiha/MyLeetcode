class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        for number in range(num1, num2 + 1):
            number = str(number)
            for i, digit in enumerate(number):
                if 1 <= i <= len(number)-2:
                    if int(number[i-1]) > int(digit) < int(number[i+1]):
                        result += 1
                    elif int(number[i-1]) < int(digit) > int(number[i+1]):
                        result += 1
        return result
    
  

                
            

        