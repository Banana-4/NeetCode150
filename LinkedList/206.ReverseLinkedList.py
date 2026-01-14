class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        while head.next:
           nodeNext = head.next
           head.next = prev
           prev = head
           head = nodeNext
        head.next = prev
        return head
