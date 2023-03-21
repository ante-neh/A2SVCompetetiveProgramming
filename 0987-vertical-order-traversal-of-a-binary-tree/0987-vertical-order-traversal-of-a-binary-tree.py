# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = {}
        
        def helper(root,row=0,col=0):
            
            if not root:
                return
            
            helper(root.left,row+1,col-1)
            if (row,col) not in self.dic:
                self.dic[(row,col)] = [root.val]
                
            else:
                self.dic[(row,col)].append(root.val)
            helper(root.right,row+1,col+1)
            
            
        helper(root)

        for key in self.dic.keys():
            self.dic[key] = sorted(self.dic[key])
            
        self.dic = sorted(self.dic.items(), key=lambda x: x[0][0])

        self.container = {}
        for key in self.dic:

            if key[0][1] not in self.container:
                self.container[key[0][1]] = key[1]
                
            else:
                self.container[key[0][1]].extend(key[1])
        ls = sorted(self.container.items(), key=lambda x: x[0])
        columns = [item[1] for item in ls]
                
        return columns