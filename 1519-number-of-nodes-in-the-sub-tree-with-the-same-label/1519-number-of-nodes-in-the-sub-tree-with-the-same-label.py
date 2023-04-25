class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        #construct tress using edges
        #since the tree has no direction ,we need to add both direction in the tree.
        tree = defaultdict(list)
        for s , e in edges:
            tree[s].append(e)
            tree[e].append(s)

        #the result of length will be returned at the end, which will be modified by dfs()
        res=[0]*n

        #node is the current node we are looping through
        #par is the node's direct parent node
        def dfs(node , par):
            nonlocal res #used to work with variables inside nested functions, where the variable should not belong to the inner function


            #using count to store the count the of occurence of each letters in sub nodes of parent nodes.
            #The size of the hashmap count will be 26 at all times, as in lowercase alphabet
            count = Counter()
            for  neighbor in tree[node]:
                #Make sure we are not going backward to its parent node thus
                if neighbor != par:
                    #update count as letter freq
                    count += dfs(neighbor,node)
            
            #Adding 1 to count with the label
            count[labels[node]] += 1
            
            #update the result
            res[node] =  count[labels[node]]

            return count
        #starting the function all over again with node 0 and pesudo parent -1
        dfs(0,-1)
        return res
                    
    