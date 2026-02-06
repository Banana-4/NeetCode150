class Node:
    def __init__(self, key: int, value: int, nextptr = None, prev = None):
        self.key = key
        self.val = value
        self.next = nextptr
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.key_node = {}
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = self.key_node.get(key, None)    
        if node:
            self.tail_it(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.key_node.get(key, None)    
        if node:
            self.tail_it(node)
            node.val = value
        else:
            if self.size + 1 > self.capacity:
                del self.key_node[self.head.key]
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            else:
                self.size += 1

            node = Node(key, value, None, self.tail)
            self.key_node[key] = node
            if self.head:
                self.tail.next = node
                self.tail = node
            else:
                self.head = self.tail = node
           
  
    def tail_it(self, node):
        if node.next:
                node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
