# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        serialized = []
        
        def dfs(node):
            if not node:
                serialized.append("n")
                return

            serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return ",".join(serialized)

    def deserialize(self, data):
        serialized = data.split(",")
        index = 0
        
        def dfs():
            nonlocal index
            if serialized[index] == 'n':
                index += 1
                return None
            
            node = TreeNode(int(serialized[index]))
            index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))