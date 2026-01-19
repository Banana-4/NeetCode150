class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, start, end = None, head, head
        win_size = 0
        while end:
            end = end.next
            win_size += 1
            if win_size > n:
                prev = start
                start = start.next
                win_size -= 1
        if not prev:
            nHead = head.next
            head.next = None
            return nHead 
        prev.next = start.next
        start.next = None
        return head
