class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        depend = defaultdict(list)
        rest = defaultdict(int)
        for i in range(len(recipes)):
            rest[recipes[i]] = len(ingredients[i])
            for ingredient in ingredients[i]:
                depend[ingredient].append(recipes[i])
        basic = set()
        for dish in supplies:
            rest[dish] = 1
            basic.add(dish)
        ans = []

        def dfs(dish):
            nonlocal ans
            rest[dish] -= 1
            if rest[dish] == 0:
                if not dish in basic:
                    ans.append(dish)
                for d in depend[dish]:
                    dfs(d)

        for d in supplies:
            dfs(d)
        return ans

