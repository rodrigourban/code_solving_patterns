"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:
1->2->5
    ->4
 ->3->6
    ->7
Output: [[1], [2,3], [4,5,6,7]]

Example 2:
12->7->9

  ->1->5
     ->10
Output: [[12], [7,1], [9, 6, 10]]
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
    We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

    1.Start by pushing the root node to the queue.
    2.Keep iterating until the queue is empty.
    3.In each iteration, first count the elements in the queue (let's call it levelSize). We will have these many nodes in the current level.
    4.Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
    5.After removing each node from the queue, insert both of its children into the queue.
    6.If the queue is not empty, repeat from step 3 for the next level.
    """
    if root is None:
        return []
    ans: list[list[int]] = []
    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level: list[int] = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        ans.append(current_level)

    print("Answer is: ", ans)
    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root) == [[1], [2, 3], [4, 5, 6, 7]]
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(5)
root.right.right = TreeNode(10)
assert solve(root) == [[12], [7, 1], [9, 5, 10]]

"""
Time complexity: O(N) N = number of nodes in tree
Space complexity: S(N) used in the queue and for the level order transversal array
"""
