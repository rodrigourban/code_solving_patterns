"""
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.

Example 1:
null
|  null  null
|  |     |
1->3----->7
   |      |
   |    ->6
   |      |
 ->2----->5
          |
        ->4


Example 2:
null
|  null  null
|  |     |
12->1---->5
    |     |
    |   ->10
    |     |
  ->7---->9
          |
        ->2

"""
from collections import deque
from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None, next: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val} {self.left} {self.right}'

    @property
    def level_order(self) -> list[int]:
        level_order: list[int] = []
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                level_order.append(current.val)
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
        return level_order


def solve(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    To solve this: Breadth First Search (BFS)
    Same approach but we need to connect the current_node
    with previous one
    """
    if root is None:
        return None

    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        previous_node = None

        for _ in range(level_size):
            current = queue.popleft()

            if previous_node:
                previous_node.next = current
            previous_node = current

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    print("Answer is: ", root.level_order)
    return root


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

assert solve(root).level_order == [1, 2, 3, 4, 5, 6, 7]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root).level_order == [12, 7, 1, 9, 2, 10, 5]


"""
Time complexity: O(N)
Space complexity: S(N)
"""
