"""
Given a set with distinct elements, find all of its distinct subsets.
Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def solve(input_list: [int]) -> [int]:
    """
    To solve this: Breadth First Search (BFS) approach
    Given set: [1, 5, 3]

    Start with an empty set: [[]]
    Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
    Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
    Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].
    """
    combinations = [[]]
    for number in input_list:
        to_append = []
        for current in combinations:
            to_append.append([*current, number])
        combinations.extend(to_append)
    return combinations


assert solve([1, 3]) == [[], [1], [3], [1, 3]]
assert solve([1, 5, 3]) == [[], [1], [5], [3],
                            [1, 5], [1, 3], [5, 3], [1, 5, 3]]

"""
Time complexity: O(2^N)
Space complexity: O(2^N)
"""
