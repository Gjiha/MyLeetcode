class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        setOfCodes = set()
        n = len(s)

        for i in range(n-k+1):
            code = s[i:i+k]
            if code not in setOfCodes:
                setOfCodes.add(code)
            print(f"CODES == {code},  SET === {setOfCodes}")
        
        if len(setOfCodes) != 2**k:
            return False

        return True
    

sol = Solution()
codes = "00110"
x = sol.hasAllCodes(codes, 2)
print(x)