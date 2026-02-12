# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        block = []
        blocks = [block]
        last = head
        while last:
            block.append(last)
            if len(block) == k:
                block = []
                blocks.append(block)
            last = last.next
        h = None
        if not blocks[-1]:
            blocks.pop()
        for i in range(len(blocks), 0, -1):
            block = blocks[i - 1]
            if len(block) == k:
                i = k - 1
                while i:
                    block[i].next = block[i - 1] 
                    i -= 1
                block[0].next = h
                h = block[-1]
            else:
                h = block[0]
        return h
