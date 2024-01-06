"""
Reverse the first k elements of a given LinkedList. 
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


def solve(head: Node, k: int) -> Node:
    """
    To solve this: In-place Reversal of a LinkedList
    This problem can be easily converted to our parent problem (Reverse sublist); 
    to reverse the first k nodes of the list, we need to pass p=1 and q=k.
    """
    p = 1
    if p == k:
        return head

    # skip p-1 steps to find a pointer to start of substring
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    p_pointer = previous

    # after reversing the linked list, k_pointer is going to be the last node of
    # the sublist
    k_pointer = current

    i = 0
    next = None
    # reverse sublist
    while current is not None and i < k - p + 1:
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
    k_pointer.next = current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(8)


assert str(solve(head, 5)) == 'head -> 5 -> 4 -> 3 -> 2 -> 1 -> 7 -> 8 -> null'


"""
Time complexity: O(n)
Space complexity: S(1)
"""
