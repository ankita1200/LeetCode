class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for index,recipe_content in enumerate(ingredients):
            for ingredient in recipe_content:
                graph[ingredient].append(recipes[index])
                indegree[recipes[index]] += 1
        
        que = deque(supplies)
        supplys = set(supplies)
        ans = []
        while que:
            currtype = que.popleft()
            if not currtype in supplys:
                ans.append(currtype)
            for neighbor in graph[currtype]:
                indegree[neighbor] -= 1
                if indegree[neighbor]==0:
                    que.append(neighbor)
            
        return ans

        
