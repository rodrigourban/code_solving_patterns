"""
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.
Ex. 1
Given node 3
Level order successor: 4
1->2->5
    ->4
 ->3->6
    ->7
    
Ex. 2
Given node 9
Level order successor: 10
12->1 ->5
      ->10
  ->7 ->9
    
Ex. 2
Given node 12
Level order successor: 7
12->1 ->5
      ->10
  ->7 ->9
"""
from collections import deque
from typing import Self, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.val} {self.left} {self.right}'


def solve(root: TreeNode, key: int) -> int | None:
    """
    To solve this: Breadth First Search (BFS)
    The only difference will be that we will not keep track of all the levels. 
    Instead we will keep inserting child nodes to the queue. As soon as we find the
    given node, we will return the next node from the queue as the level order successor.
    """
    queue: deque[TreeNode] = deque()
    queue.append(root)

    while queue:
        current: TreeNode = queue.popleft()

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

        if current.val == key:
            break

    # popleft on empty deque raises index error
    ans: int | None = queue[0].val if queue else None
    print("Answer is: ", ans)
    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
assert solve(root, 3) == 4

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.right = TreeNode(5)
root.right.left = TreeNode(10)
assert solve(root, 9) == 10
assert solve(root, 12) == 7


"""
Time complexity: O(N) N = number of nodes in tree
Space complexity: S(N)
"""
