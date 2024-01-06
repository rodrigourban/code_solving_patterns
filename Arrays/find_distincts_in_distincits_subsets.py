"""
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [[], [1], [3], [1,3]]
Example 2:

Input: [1, 5, 3]
Output: [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]]
"""


def solve(nums: list[int]) -> list[list[int]]:
    """
    To solve this: Breadth First Search (BFS)
    Given set: [1, 5, 3]

    Start with an empty set: [[]]
    Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
    Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
    Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].
    """
    ans: list[list[int]] = [[]]
    for element in nums:
        to_add: list[list[int]] = []
        for sub_element in ans:
            print(sub_element, " , ")
            to_add.append([*sub_element, element])
        ans.extend(to_add)

    print("Answer is: ", ans)
    return ans


assert solve([1, 3]) == [[], [1], [3], [1, 3]]
assert solve([1, 5, 3]) == [[], [1], [5], [1, 5], [3],
                            [1, 3], [5, 3], [1, 5, 3]]


"""
Time complexity: O(2^N) N being the total number of elements in the array
Space complexity: S(2^N) Output list
"""
