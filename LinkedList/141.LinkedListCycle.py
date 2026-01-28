class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = turtle = head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True
        return False
