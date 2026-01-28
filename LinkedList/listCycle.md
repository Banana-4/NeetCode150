# 141. Linked List Cycle

## Problem:
    Given a head to a linked list find out if the list has a cycle.
    return true if ther is a cycle otherwise false.
    
## What is a Cycle?
    Cycle in linked list is when a node points to a previous node.
    Cycle is when iterating from the head a null node while never be reached.
    When two nodes point to the same node.
    
## Edge Cases:
    Head is null.
    Node points to it self.
    
## Solution 1 - hash map:

### Invariant:
    The current node will never be null.

### Algorithm:
    A hash map stores the visited nodes.
    while current:
        if current is visited:
            There is a cycle return true.
        else:
            add it to the visited nodes.
   If the current node is null, there is no cycle in the list return false.
   
### Time Complexity:
    O(n)

### Space Complexity:
    O(n)

### Code:
``` Python3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

```

## Solution 2 - Floyd's Turtle and rabbit algorithm:
    Two pointer solution. Fast pointer called rabbit and slow pointer called turtle.
    The idea is to use two pointers in the list that will be racing against each other.
    The turtle and rabbit start from the same position.
### Invariant:
    The turtle will never reach null before the rabbit does.
    The turtle and rabbit will never meet again in the list iteration.
    
### Insight:
    The key  of the algorithm is that there is no escape from a list cycle.
 
### Algorithm:
    while rabbit and rabbit.next:
        turtle moves one node
        rabbit moves two nodes
        if rabbit and turtle are at the same node:
            there is a cycle return true.
    if rabbit is null or rabbit.next is null the race is over the rabbit won. Ok there is no cycle return false.
   
### Time Complexity:
O(n)

### Space Complexity:
O(1)

### Code:

``` Python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = turtle = head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True
        return False

```

## Conclusion:
    1. Floyd's algorithm is used for systems for a solution to a interview question and when the linked lists use a lot of the systems memory.
    2. Hash mapping is better in situations where there is enough memory to store duplicated lists.
