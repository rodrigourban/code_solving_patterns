"""
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

Example 1:
Minimum depth 2
1->3
 ->2->5
    ->4

Example 2:
Minimum depth: 2
12->1->5
     ->10
  ->7

Example 3:
Minimum depth: 3
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
    Same approach but instead of keeping track of all the nodes in a level, we will only track the
    depth of the tree. As soon as we find our first leaf node, that level will 
    represent the minimum depth of the tree.
    """
    if root is None:
        return 0

    queue: deque[TreeNode] = deque()
    queue.append(root)
    min_depth = 0
    while queue:
        min_depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()

            if current.left is None and current.right is None:
                print("Answer is: ", min_depth)
                return min_depth

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    print("Answer is: ", min_depth)
    return min_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

assert solve(root) == 2

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == 2

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(11)
assert solve(root) == 3

"""
Time complexity: O(N)
Space complexity: S(N)
"""
