"""
You are given the root of a binary tree with unique values, and an integer start. 
At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
"""

from collections import deque, defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.val} {self.left} {self.right}'


def binary_tree_to_graph(root: TreeNode) -> defaultdict:
    """
    To transform a binary tree to graph we need
    1. Initialize the deque with our root.
    2.Look through the queue
        a. Pop the last element added
        b. Check if it has a parent, add it
        to currents list of vertex, and also
        add current node to parents key in graph
        (Both are connected to each other)
        c. If current node has a left, add the left to the
        queue with current as the parent
        If current node has a right, add the right to the
        queue with current as the parent
    This will populate every vertex of the graph
    """
    graph = defaultdict(list)
    queue = deque([(root, None)])
    while queue:
        current, parent = queue.popleft()
        if parent:
            graph[current.val] += [parent]
            graph[parent.val] += [current]
        if current.left:
            queue.append([current.left, current])
        if current.right:
            queue.append([current.right, current])

    return graph


def bfs(graph, root: int) -> int:
    """
    Return the farthest node and its distance from node u
    """
    visited = defaultdict(bool)

    # visited = [False for _ in range(
    #     len(graph) + 1)]  # get number of vertices on graph
    # # get number of vertices on graph
    # distance = [-1 for _ in range(len(graph))]
    distance = defaultdict(int)

    distance[root] = 0
    visited[root] = True
    queue = deque()
    queue.append(root)

    while queue:

        front = queue.popleft()

        for i in graph[front]:
            current_val = i.val
            if not visited[current_val]:
                visited[current_val] = True

                distance[current_val] += distance[front] + 1

                queue.append(current_val)

    return max(distance.values())


def solve(root: Optional[TreeNode], start: int) -> int:
    """
    We need to the max distance between start and a node.
    We can use BFS over a graph for this, but first we need
    to transform the binary tree into a graph.
    Then, we need the farthest node from the tree.
    Once we have it, calculate the distance from start to this node
    using BFS, the max is going to be our answer
    """

    if root:  # can remove this later
        graph = binary_tree_to_graph(root)

        # get longest distance from tree
        longest_distance = bfs(graph, start)

        return longest_distance
    else:
        return 0


root = TreeNode(1)
root.left = TreeNode(5)
infected = TreeNode(3)
root.right = infected
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
assert solve(root, 3) == 4

root = TreeNode(1)
assert solve(root, 0) == 0
