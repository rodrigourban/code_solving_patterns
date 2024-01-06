"""
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the 
new head of the reversed LinkedList.
Original List: 
    head ->  2->4->6->8->10->null  
Reversed List: 
    null<-2<-4<-6<-8<-10 <- head  

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


def solve(head: Node) -> Node:
    """
    To solve this: In-place Reversal of a LinkedList
    To reverse a LinkedList, we need to reverse one node at a time. We will start with a variable
    current which will initially point to the head of the LinkedList and a variable previous which
    will point to the previous node that we have processed; initially previous will point to null.

    In a stepwise manner, we will reverse the current node by pointing it to the previous before moving
    on to the next node. Also, we will update the previous to always point to the previous node that we 
    have processed. Here is the visual representation of our algorithm:
    """
    current = head
    previous: Node | None = None
    next: Node | None = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    print("Answer is: ", previous)
    return previous  # type: ignore


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

assert str(solve(head)) == 'head -> 10 -> 8 -> 6 -> 4 -> 2 -> null'


"""
Time complexity: O(N)
Space complexity: S(1)
"""
