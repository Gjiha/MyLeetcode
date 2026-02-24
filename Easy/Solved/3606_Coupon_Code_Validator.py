class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        n = len(code)
        electronicsList = []
        groceryList = []
        pharmacyList = []
        restaurantList = []

        for i in range(n):
            doable = True
            for char in code[i]:
                if not('a'<=char.lower()<='z') and not(char =='_') and not('0'<=char<='9'):
                    doable = False
            if isActive[i] and doable and code[i]:
                if businessLine[i] == 'electronics':
                    electronicsList.append(code[i])
                elif businessLine[i] == 'grocery':
                    groceryList.append(code[i])
                elif businessLine[i] == 'pharmacy':
                    pharmacyList.append(code[i])
                elif businessLine[i] == 'restaurant':
                    restaurantList.append(code[i])
        electronicsList.sort()
        groceryList.sort()
        pharmacyList.sort()
        restaurantList.sort()
        returnList = electronicsList + groceryList + pharmacyList + restaurantList
        return returnList

c = ["pBXoMqBU0_aMgc9F8dy6TaSzza3KjSJFjxZa_NuyMjzEBR7fJNwpGHh7lzuoZvQeEUeo6YumHmIOjjchXlzSVa4ItdyDOImQgm","P8rIIUl35MW8yrqRbO0N_IITptYOxz9tOCbPL6d1aIF_hM2sapaDtUzNpmAZRmJQB1WgjLh8bdYADuSRSU21OzttUkq73qiA66","aFWkYookQlHYMXzhVGxbnrXIl1810ws3qHtketHSECHqJoktWXVZGc6ZyeOuzA_VL9zFL9znpIHwbkwJF2bOPQqsz3_0PYgETJ"]
b = ["pharmacy","invalid","pharmacy"]
a = [True,True,True]

sol = Solution()
print(sol.validateCoupons(c,b,a))

