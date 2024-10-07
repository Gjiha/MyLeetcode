class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        i = 0
        j = len(skill) - 1

        sumToMaintain = skill[i] + skill[j]

        sumOfChemistry = 0

        while i < j:
            
            sumOfSkill = skill[i] + skill[j]

            if sumToMaintain != sumOfSkill:
                return -1

            sumOfChemistry += skill[i] * skill[j]

            i += 1
            j -= 1
        
        
        return sumOfChemistry
        


        