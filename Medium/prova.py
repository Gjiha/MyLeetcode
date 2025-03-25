class Solution:

    def checkRecipe(self,recipe, dictOfRecipe, setOfSupplies, visited=set()) -> bool:
        for ingridient in dictOfRecipe[recipe]:
            if ingridient in visited:
                return False, {}
            
            elif ingridient in setOfSupplies:
                continue

            elif ingridient in dictOfRecipe and ingridient not in setOfSupplies:
                visited.add(recipe)
                if not self.checkRecipe(ingridient, dictOfRecipe, setOfSupplies, visited):
                    return False, {}
                visited = set()
                setOfSupplies.add(ingridient)


    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        dictOfRecipe = {}

        for i, recipe in enumerate(recipes):
            dictOfRecipe[recipe] = set(ingredients[i])
        
        setOfSupplies = set(supplies)

        



sol = Solution()
x = sol.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"])