# LeetCode 19. Remove Nth Node From End of List

## Problem:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
## Data:
### Input:
    1. The head of a linked list.
    2. n - the number of nodes away from the tail of the list
### Output:
    list without the nth node from the end.

## Constrains:
sz ::= number of nodes in the list
1. 1 <= sz <= 30
2. 0 <= Node.val <= 100
3. 1 <= n <= sz

## Solution:
### Naive aproach:
Find out the size of the list by counting the nodes.
Convert n into the node positon from the start n = size - n + 1
then use the standart method for node removal for linked lists.
#### Space: 
O(1)

#### Time:
2n
O(n), n to count the nodes and  n time to remove the nodes.

### Storing the nodes into a array:
Store the nodes one by one in a array.
Then take the n - 1 node and connect it to the n + 1 node, then destroy the nth node.
#### Space:
O(n)
#### Time:
n
O(n)

### Best solution:
Sliding windows,
Use 3 pointers to nodes, one to point at the start of the window of size n, second to point to the end of the window and the third to point to starts node previous node.
Once the end node reaches the tail, remove the nth start node by making the prev node point to its next and the start node to point to null.
#### Space:
O(1)
#### Time:
O(n)
#### Code:
```
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
```
