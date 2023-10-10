class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def moveToHead(self, node):

        if self.head == self.tail or self.head == node:
            return

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        
        node.prev.next = node.next
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def addNode(self, key, val):
        node = Node(key, val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node
  
    def removeTail(self):
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.linkedList = LinkedList()
        self.lruMap = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
            
        if key not in self.lruMap:
            return -1
        
        node = self.lruMap.get(key)
        val = node.val
        self.linkedList.moveToHead(node)

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.lruMap:
            node = self.lruMap[key]
            node.val = value
            self.linkedList.moveToHead(node)
            return
            
        if self.capacity == len(self.lruMap):
            del self.lruMap[self.linkedList.tail.key]
            self.linkedList.removeTail()
            
        node = self.linkedList.addNode(key, value)
        self.lruMap[key] = node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)