from typing import Self
"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3
Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
Example 3:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
"""


class Node:
    def __init__(self, value: int, next: Self | None = None) -> None:
        self.value = value
        self.next = next


def solve(head: Node) -> Node:
    """
    To solve this: Fast Slow Pointer
    We can use the Fast & Slow pointers method such that the fast pointer is 
    always twice the nodes ahead of the slow pointer. This way, when the fast 
    pointer reaches the end of the LinkedList, the slow pointer will be pointing 
    at the middle node.
    """
    pointer_1, pointer_2 = head, head

    while pointer_2 is not None and pointer_2.next is not None:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next.next

    print("Answer is: ", pointer_1.value)
    return pointer_1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
assert solve(head).value == 3

head.next.next.next.next.next = Node(6)
assert solve(head).value == 4

head.next.next.next.next.next.next = Node(7)
assert solve(head).value == 4

"""
Time complexity: O(n)
Space complexity: S(1)
"""
