"""
Given the head of a LinkedList and two positions p and q, reverse the LinkedList from position p to q.

Original List: p=2, q=4
Example: 
 head -> 1->2->3->4->5 -> null
 head -> 1->4->3->2->5 -> null  
"""

from typing import Self


class Node:
    def __init__(self, value: int, next: Self | None = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        rep = 'head ->'
        temp = self
        while temp is not None:
            rep += f' {temp.value} ->'
            temp = temp.next
        rep += ' null'
        return rep


def solve(head: Node, p: int, q: int) -> Node:
    """
    To solve this: In-place Reversal of a LinkedList
    1.Skip the first p-1 nodes, to reach the node at position p.
    2.Remember the node at position p-1 to be used later to connect with the reversed sub-list.
    3.Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
    4.Connect the p-1 and q+1 nodes to the reversed sub-list.
    """
    if p == q:
        return head

    # skip p-1 steps to find a pointer to start of substring
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    p_pointer = previous

    # after reversing the linked list, q_pointer is going to be the last node of
    # the sublist
    q_pointer = current

    i = 0
    next = None
    # reverse sublist
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect first part
    if p_pointer is not None:
        # previous is the first node of the substring
        p_pointer.next = previous
    # p == 1, meaning we are changing the head
    else:
        head = previous

    # connect last part
    q_pointer.next = current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


assert str(solve(head, 2, 4)) == 'head -> 1 -> 4 -> 3 -> 2 -> 5 -> null'


"""
Time complexity: O(n)
Space complexity: S(1)
"""
