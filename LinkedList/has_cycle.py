"""
Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not.
Following LinkedList has a cycle: 
head->1->2->3->4->5->6
         ^-----------|
Following LinkedList doesn't have a cycle: 
head->2->4->6->8->10->null 
"""


class Node:
    def __init__(self, value: int, next: Self | None = None) -> None:
        self.value = value
        self.next = next


def solve(head: Node) -> bool:
    """
    To solve this: Two pointers
    1 fast pointer (2 steps) 1 slow pointer (1 step)
    Imagine we have a slow and a fast pointer to traverse the LinkedList. In each iteration, 
    the slow pointer moves one step and the fast pointer moves two steps. This gives us two conclusions:
    1. If the LinkedList doesn't have a cycle in it, the fast pointer will reach the end of the LinkedList 
    before the slow pointer to reveal that there is no cycle in the LinkedList.
    2. The slow pointer will never be able to catch up to the fast pointer if there is no cycle in the LinkedList.
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # found
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
assert solve(head) == False

head.next.next.next.next.next.next = head.next.next
assert solve(head) == True

head.next.next.next.next.next.next = head.next.next.next
assert solve(head) == True

"""
Time complexity: O(N)
Space complexity: O(1)
"""
