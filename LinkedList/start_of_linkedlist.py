"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
            ^Cycle start
head->1->2->3->4->5->6
            ^--------|
               ^Cycle start
head->1->2->3->4->5->6
               ^-----|
      ^Cycle start      
head->1->2->3->4->5->6
      ^--------------|
"""


from typing import Self


class Node:
    def __init__(self, value: int, next: Self | None = None) -> None:
        self.value = value
        self.next = next


def calculate_cycle_length(slow_pointer: Node) -> int:
    current = slow_pointer
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow_pointer:
            break
    return cycle_length


def find_cycle_length(head: Node) -> int:
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # found
            return calculate_cycle_length(slow)
    return 0


def solve(head: Node) -> Node:
    """
    To solve this: Fast and Slow Pointer
    If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
    1.Take two pointers. Let's call them pointer1 and pointer2.
    2.Initialize both pointers to point to the start of the LinkedList.
    3.We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle.
    Let's assume that the length of the cycle is K nodes.
    4.Move pointer2 ahead by K nodes.
    5.Now, keep incrementing pointer1 and pointer2 until they both meet.
    6.As pointer2 is K nodes ahead of pointer1, which means, pointer2 must have completed one loop 
    in the cycle when both pointers meet. Their meeting point will be the start of the cycle.
    """
    pointer_1: Node | None = head
    pointer_2: Node | None = head
    cycle_length = find_cycle_length(head)
    while cycle_length > 0:
        pointer_2 = pointer_2.next
        cycle_length -= 1
    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    print("Answer is: ", pointer_1.value)
    return pointer_1  # type: ignore


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
assert solve(head).value == 3

head.next.next.next.next.next.next = head.next.next.next
assert solve(head).value == 4

head.next.next.next.next.next.next = head
assert solve(head).value == 1


"""
Time complexity: O(N)
Space complexity: S(1)
"""
