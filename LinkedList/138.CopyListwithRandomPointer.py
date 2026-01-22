class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        current = head
        groups = {}
        while current:
            node = Node(current.val)
            groups[current] = node
            current = current.next
        current = head
        while current:
            groups[current].random = groups.get(current.random, None)
            groups[current].next = groups.get(current.next, None)
            current = current.next
        return groups.get(head, None)
