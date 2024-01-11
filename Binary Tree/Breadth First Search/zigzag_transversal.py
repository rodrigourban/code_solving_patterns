"""
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the 
following levels.

Example 1:
1->3->7
    ->6
 ->2->5
    ->4
 
Output: [[1], [3,2], [4,5,6,7]]

Example 2:
12->1->5
     ->10
  ->7->9
     ->2
Output: [[12], [1, 7], [2, 9, 10, 5]]
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


def solve(root: Optional[TreeNode]) -> list[list[int]]:
    """
    To solve this: Breadth First Search (BFS)
    We can do BFS but we push the elements left or right
    depending in a bool append_order that toggles value
    after append.
    """
    if root is None:
        return []
    ans: list[list[int]] = []
    queue: deque[TreeNode] = deque()
    queue.append(root)
    append_order = False
    while queue:
        level_size = len(queue)
        level_nodes: deque[int] = deque()
        for _ in range(level_size):
            current_node = queue.popleft()

            if append_order:
                level_nodes.appendleft(current_node.val)
            else:
                level_nodes.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
        ans.append(list(level_nodes))
        append_order = not append_order

    print("Answer is: ", ans)
    return ans


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root) == [[1], [3, 2], [4, 5, 6, 7]]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert solve(root) == [[12], [1, 7], [9, 2, 10, 5]]


"""
Time complexity: O(N)
Space complexity: S(N)
"""
