class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        n = len(needle)
        while i < len(haystack):
            if i + n > len(haystack):
                return -1 
            if haystack[i : i + n] == needle:
                return i
            i += 1
        return -1
    
sol = Solution()
print(sol.strStr("abutsadw", "sad"))