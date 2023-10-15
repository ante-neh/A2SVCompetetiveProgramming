class Solution:
    def dfs(self, node, dest, adj, vis, res, cal):
        vis[node] = 1
        if node == dest:
            res[0] = cal
            return True

        if node in adj:
            for nod, val in adj[node]:
                if vis[nod] == 0:
                    if self.dfs(nod, dest, adj, vis, res, cal * val):
                        return True
        return False

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        i = 0
        for u, v in equations:

            if u in adj: adj[u].append([v, values[i]])
            else: adj[u] = [[v, values[i]]]

            if v in adj: adj[v].append([u, 1/values[i]])
            else: adj[v] = [[u, 1/values[i]]]

            i += 1
        
        ans = []
        for u, v in queries:
            vis = { key: 0 for key in adj}
            res = [-1.0]

            if u in adj and v in adj:
                    if self.dfs(u, v, adj, vis, res, 1):
                        ans.append(res[0])
                    else: ans.append(-1.0)
            else: ans.append(-1.0)
        
        return ans