class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newHead = Node(head.val, head.next, head.random)
        node = newHead
        prev = node
        head.copy = node
        head = head.next
        
        while head:
            node = Node(head.val, head.next, head.random)
            prev.next = node
            prev = node
            head.copy = node
            head = head.next
        node =newHead
        while node:
            node.random = node.random.copy if node.random else None
            node = node.next
        return newHead
