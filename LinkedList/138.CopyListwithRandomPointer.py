class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1, None, None)
        node = newHead
        prev = newHead
        while head:
            node = Node(head.val, head.next, head.random)
            prev.next = node
            prev = node
            head.copy = node
            head = head.next
        newHead = newHead.next
        node = newHead
        while node:
            node.random = node.random.copy if node.random else None
            node = node.next
        return newHead
