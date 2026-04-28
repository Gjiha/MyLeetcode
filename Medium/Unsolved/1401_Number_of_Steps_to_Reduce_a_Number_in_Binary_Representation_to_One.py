class Solution:
    def numSteps(self, s: str) -> int:
        listString = list(s)
        n = len(listString) - 1
        i = n
        count = 0
        report = False
        while i > 0:
            if listString[i] == 0:
                if report:
                    report = False
                    count += 1
                count += 1
                i -= 1
            elif listString[i] == 1:
                count += 2
                i -= 1