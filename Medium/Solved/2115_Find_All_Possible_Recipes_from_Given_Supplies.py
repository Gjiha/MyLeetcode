class Solution:

    def checkRecipe(self,recipe, dictOfRecipe, setOfSupplies, visited) -> bool:
        newIngridients = set()
        visited.add(recipe)
        
        for ingridient in dictOfRecipe[recipe]:
            if ingridient in visited:
                return False, None
            
            elif ingridient in setOfSupplies:
                continue

            elif ingridient in dictOfRecipe and ingridient not in setOfSupplies:

                boolean, newIngridients = self.checkRecipe(ingridient, dictOfRecipe, setOfSupplies, visited)

                if not boolean:
                    return False, None
                
                visited.remove(ingridient)
                setOfSupplies.add(ingridient)
                newIngridients.add(ingridient)
            
            elif ingridient not in setOfSupplies:
                return False, None

        
        return True , newIngridients



    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        listToOutput = []

        dictOfRecipe = {}
        setOfSupplies = set(supplies)

        for i, recipe in enumerate(recipes):
            dictOfRecipe[recipe] = set(ingredients[i])
        
        for recipe in dictOfRecipe:
            visited = set()
            boolean, newIngridients = self.checkRecipe(recipe, dictOfRecipe, setOfSupplies, visited)
            if boolean:
                listToOutput.append(recipe)
                setOfSupplies.add(recipe)
                setOfSupplies.intersection(newIngridients)

        return listToOutput
        

        



sol = Solution()
x = sol.findAllRecipes(["burger","bread","sandwich"], [["sandwich","meat","bread"],["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"])
print(x)