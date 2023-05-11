class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        queue = deque()
        indegree = {}
        recipesCreated = []
        for supply in supplies:
            queue.append(supply)
            
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] = 1 + indegree.get(recipes[i], 0)
                
        while queue:
            recipe = queue.popleft()
            if recipe in recipes:
                recipesCreated.append(recipe)
            for neighbor in graph[recipe]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return recipesCreated
            