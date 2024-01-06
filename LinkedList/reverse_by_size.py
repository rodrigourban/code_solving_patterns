from typing import Self
"""
Given a LinkedList with n nodes, reverse it based on its size in the following way:

If n is even, reverse the list in a group of n/2 nodes.
If n is odd, keep the middle node as it is, reverse the first n/2 nodes and
reverse the last n/2 nodes.

Example 1: even n
    head -> 1->2->3->4->5->6->7->8 -> null
    head -> 4->3->2->1->8->7->6->5 -> null
Example 2: odd n
    head -> 1->2->3->4->5->6->7 -> null  
    head -> 3->2->1->4->7->6->5 -> null  
"""


class Node:
    def __init__(self, value: int, next: Self | None = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        rep = 'head->'
        temp = self
        while temp is not None:
            rep += f'{temp.value}->'
            temp = temp.next
        rep += 'null'
        return rep
        # return str(self.value)


def get_middle_node(head: Node) -> Node | None:
    # We use Fast Slow Pointer, once fast pointer reaches end of linked list
    # it means that slow pointer is in the middle
    pointer_1, pointer_2 = head, head

    while pointer_2 is not None and pointer_2.next is not None:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next.next

    return pointer_1


def get_linked_list_length(head: Node) -> int:
    i = 0
    pointer = head
    while pointer is not None:
        pointer = pointer.next
        i += 1
    return i


def reverse_linked_list_k(head: Node, k: int, middle_node=None) -> Node:
    if k <= 1 or head is None:
        return head

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

        if current is None:
            q_pointer.next = current
            break

        # check middle
        if middle_node is not None and current.next == middle_node.next:
            q_pointer.next = middle_node
            current = middle_node.next
            middle_node.next = current
            previous = middle_node
            continue

        previous = q_pointer

    return head


def solve(head: Node) -> Node:
    """
    To solve this: In-place Reversal of a LinkedList
    When n is even we can perform the following steps:

    Reverse first n/2 nodes: head = reverse(head, 1, n/2)
    Reverse last n/2 nodes: head = reverse(head, n/2 + 1, n)

    When n is odd, our algorithm will look like:
    head = reverse(head, 1, n/2)
    head = reverse(head, n/2 + 2, n)
    Please note the function call in the second step. We're skipping two elements as we will be 
    skipping the middle element.

    """
    if head is None:
        return head

    # first we get the linked list length
    list_length = get_linked_list_length(head)

    if list_length % 2 == 0:
        # even
        print("List length is even")
        return reverse_linked_list_k(head, list_length // 2)
    else:
        # odd
        print("List length is odd")
        middle_node = get_middle_node(head)
        return reverse_linked_list_k(head, list_length // 2, middle_node=middle_node)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
print(str(solve(head)))
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
print(str(solve(head)))


"""
Time complexity: O(n) -> length of list n, reverse n, middle list n -> 3n
Space complexity: S(1)
"""
