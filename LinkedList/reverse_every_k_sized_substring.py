from typing import Self

"""
Given the head of a LinkedList and a number k, reverse every k sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than k elements, reverse it too.
Example: k=3
Original List: head -> 1->2->3->4->5->6->7->8 -> null
Reversed sub-list: head -> 3->2->1->6->5->4->8->7 -> null  
"""


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


def solve(head: Node | None, k: int) -> Node | None:
    """
    To solve this: In-place Reversal of a LinkedList
    This problem is quite similar to Reverse a Sub-list. The only difference is that we have to reverse all the sub-lists. 
    We can use the same approach, starting with the first sub-list (i.e. p=1, q=k) 
    and keep reversing all the sub-lists of size k.
    (Steps to Reverse a sub-list)
    1.Skip the first p-1 nodes, to reach the node at position p.
    2.Remember the node at position p-1 to be used later to connect with the reversed sub-list.
    3.Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
    4.Connect the p-1 and q+1 nodes to the reversed sub-list.
    """
    if k <= 1 or head is None:
        return head

    # Instead of reversing one sub-list, we reverse them all
    current, previous = head, None
    while True:
        p_pointer = previous
        q_pointer = current

        i = 0
        next = None
        # reverse sublist
        while current is not None and i < k:
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

        if current is None:
            break

        previous = q_pointer

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)


assert str(solve(head, 3)) == 'head -> 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null'


"""
Time complexity: O(n)
Space complexity: S(1)
"""
