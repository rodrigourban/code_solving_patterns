"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., 
the lowest level comes first. You should populate the values of all nodes in each level from 
left to right in separate sub-arrays.

Example 1:
1->3->7
    ->6
 ->2->5
    ->4
 
Output: [[4,5,6,7], [2,3], [1]]

Example 2:
12->1->5
     ->10
  ->7->9
Output: [[9, 5, 10], [7,1], [12]]

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


def solve(root: Optional[TreeNode]) -> deque[list[int]]:
    """
    To solve this: Breadth First Search (BFS)
    Same approach but instead of appending the current level at the end, 
    we will append the current level at the beginning of the result list.
    We can use a deque for this.
    """
    ans: deque[list[int]] = deque()

    if root is None:
        return ans

    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level: list[int] = []

        for _ in range(level_size):
            current: TreeNode = queue.popleft()
            current_level.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        ans.appendleft(current_level)

    print("Answer is: ", ans)
    return ans


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root) == deque([[4, 5, 6, 7], [2, 3], [1]])

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == deque([[9, 10, 5], [7, 1], [12]])


"""
Time complexity: O(N)
Space complexity: S(N)
"""
