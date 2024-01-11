"""
Given a binary tree, find its maximum depth (or height).

Example 1:
Maximum depth 3
1->3
 ->2->5
    ->4

Example 2:
Maximum depth: 3
12->1->5
     ->10
  ->7

Example 3:
Maximum depth: 4
12->1->5
     ->10->11
  ->7->9

"""
from collections import deque
from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.val} {self.left} {self.right}'


def solve(root: Optional[TreeNode]) -> int:
    """
    To solve this: Breadth First Search (BFS)
    Same approach but instead of returning as soon as we find a leaf node,
    we will keep traversing for all the levels, incrementing maximumDepth each time we 
    complete a level
    """
    if root is None:
        return 0

    queue: deque[TreeNode] = deque()
    queue.append(root)
    max_depth = 0
    while queue:
        max_depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    print("Answer is: ", max_depth)
    return max_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

assert solve(root) == 3

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == 3

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(11)
assert solve(root) == 4

"""
Time complexity: O(N)
Space complexity: S(N)
"""
