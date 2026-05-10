class Solution:
    def rotatedDigits(self, n: int) -> int:
        setOfNotValuable = set(['3', '4', '7'])
        setOfValuable = set(['2', '5', '6', '9'])
        count = 0
        for i in range(1, n + 1):
            setNum = set(str(i))
            if len(setNum.intersection(setOfNotValuable)) == 0:
                if len(setNum.intersection(setOfValuable)) >= 1:
                    count += 1
        return count 
    
