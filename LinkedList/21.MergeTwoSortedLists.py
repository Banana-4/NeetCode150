class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while list1 or list2:
            if not list1:
                node.next = list2
                list2 = list2.next
            elif not list2:
                node.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node = head.next
        head.next = None
        return node
