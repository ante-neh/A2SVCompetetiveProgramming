
class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        
class MapSum:

    def __init__(self):
        self.trieMap = TrieMap()

    def insert(self, key: str, val: int) -> None:
        self.trieMap.insert(key, val)

    def sum(self, prefix: str) -> int:
        res = self.trieMap.keyWithPrefix(prefix)

        return 0 if not res else sum(res)



class TrieMap:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key, val):
        node = self.root

        for letter in key:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.val = val
    
    def keyWithPrefix(self, prefix):
        res = []

        node = self.getNode(self.root, prefix)

        if not node:
            return res

        self.traverse(node, [], res)
        return res
        
    def getNode(self, node, word):

        for letter in word:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node

    def traverse(self, node, path, res):
        if not node:
            return

        if node.val != 0:
            res.append(node.val)
        
        for letter in node.children:
            path.append(node)
            self.traverse(node.children[letter], path, res)
            path.pop()


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)