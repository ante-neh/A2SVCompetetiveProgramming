class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = {}
        queue = deque()
        order = set()
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                incoming[recipes[i]] = 1 + incoming.get(recipes[i], 0)
                
        for supply in supplies:
            queue.append(supply)
                    
        while queue:
            recipe = queue.popleft()
            if recipe in recipes:
                order.add(recipe)   
            for neighbor in graph[recipe]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    
        return order
            
            