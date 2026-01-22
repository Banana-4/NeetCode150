# LeetCode 138.

## Problem:
Deep copy a singly linked list with a additonal random pointer that points to null or some random node of the list.
The copied list should have no pointers that point to the original list.

## DATA:

### Node:
    value: int
    next: Node pointer
    random: Node pointer

## Invariant:
    The copied list should always be a valid single linked list.

## Edge Cases:
1. List empty.
2. The node points to it self with the random pointer.
3. The node random pointer points to the same node as the next pointer. 

## The main problem:
    While i can use the input lists random pointer to go to a node in the input list, in the new node i can do this ther are three reasons for that:
        1. The new random node may not be created yet.
        2. If I create a new random node, ther is no way of checking where should it be put in the new list or even if the new random node is the same as the parent node.
        3. Creating new random nodes would mean that i need to create a new random node for each random node created, this description is even to hard to read i can imagen how hard would it be to write a good algorithm for this.

## My solution:
    Uses a dummy node.
    I the only thing left is to group each new node created with the node that it copies. 
    My choose of grouping the new nodes with the input nodes is to use the Python language feature that allows a new property to be added to a object at runtime.
    I added a new member variable called copy to the input nodes that stores a reference to the new copied node.
    Now the new list can be iterated to replace the input random nodes with the copied node that is stored inside it. 

### Time complexity:
O(n)
### Memory complexety:
O(n)

### Code:
``` Python
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
```


## Hash map solution:
This solution is a two pass algorithm.
The only difrence is that no change is done to the original list, the input and copy nodes are group by using the Python dict object, key input node : value its copy node

### Time complexity:
O(n)
### Memory complexety:
O(n)

### Code:
``` Python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1, None, None)
        node = newHead
        prev = newHead
        groups = {}
        while head:
            node = Node(head.val, head.next, head.random)
            prev.next = node
            prev = node
            groups[head] = node
            head = head.next
        node = newHead
        while node:
            node.random = groups.get(node.random, None)
            node = node.next
        return newHead.next
```
## Hash map simplified solution:
This solution is a two pass algorithm.
First pass:
    iterate through the list =, creating a new node with only the current nodes vlaue copied into it, and group the new node with the old one in a hash map, old_node : new_node
Second pass:
    Iterate again the list, but this time seting the new nodes next and random pointers to the nodes that are associated with the keys
    current.next and current.random.
return the node that is mapped to the head node.
### Time complexity:
O(n)
### Memory complexety:
O(n)

### Code:
``` Python
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
```
