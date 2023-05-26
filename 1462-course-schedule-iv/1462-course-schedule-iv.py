class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            course, prerequisite = prerequisite
            graph[course].append(prerequisite)

        
        def dfs(source, target):
            visited = set()
            stack = [source]

            while stack:
                course = stack.pop()

                if course in visited:
                    continue

                visited.add(course)
                if course == target:
                    return True

                stack.extend(graph[course])

            return False

        results = []
        for query in queries:
            source, target = query
            results.append(dfs(source, target))

        return results