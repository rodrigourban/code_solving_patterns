"""
Find the largest value on each level of a binary tree.

Example 1:
1->3->7
    ->6
 ->2->5
    ->4
 
Output: 7

Example 2:
12->1->5
     ->10
  ->7->9
     ->2
Output: 12
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
    Same approach but instead of having a running sum we will track the maximum value of each level.
        maxValue = max(maxValue, currentNode.val)
    """
    if root is None:
        return 0

    ans: int = 0
    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        max_number_in_level = 0

        for _ in range(level_size):
            current_node = queue.popleft()
            max_number_in_level = max(
                max_number_in_level,
                current_node.val
            )

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
        ans = max(
            ans,
            max_number_in_level
        )
    print("Answer is: ", ans)
    return ans


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root) == 7

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == 12


"""
Time complexity: O(N)
Space complexity: S(N)
"""
