"""
Given a binary tree, populate an array to represent the averages of all of its levels.

Example 1:
1->3->7
    ->6
 ->2->5
    ->4
 
Output: [1, 2.5, 5.5]

Example 2:
12->1->5
     ->10
  ->7->9
     ->2
Output: [12, 4, 6.5]
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


def solve(root: Optional[TreeNode]) -> list[float]:
    """
    To solve this: Breadth First Search (BFS)
    Same approach but, we accumulate the sum of the values of all nodes in each level. 
    Then we add the average (level_sum / level_size) to our ans array
    """
    if root is None:
        return []

    ans: list[float] = []
    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.val

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
        ans.append(level_sum / level_size)

    print("Answer is: ", ans)
    return ans


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root) == [1.0, 2.5, 5.5]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == [12.0, 4.0, 6.5]


"""
Time complexity: O(N)
Space complexity: S(N)
"""
