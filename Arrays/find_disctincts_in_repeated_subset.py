"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [[], [1], [3], [1,3], [3,3], [1,3,3]]
Example 2:

Input: [1, 5, 3, 3]
Output: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]]
"""


def solve(nums: list[int]) -> list[list[int]]:
    """
    To solve this: Breadth First Search (BFS)
    Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
    Follow the same BFS approach but whenever we are about to process a duplicate (i.e., 
    when the current and the previous numbers are same),
    instead of adding the current number (which is a duplicate) to all the existing subsets, only add 
    it to the subsets which were created in the previous step.
    """
    subsets: list[list[int]] = [[]]
    sorted_array = sorted(nums)
    end_index = 0
    for i in range(len(sorted_array)):
        start_index = 0
        if i > 0 and sorted_array[i-1] == sorted_array[i]:
            # duplicate
            start_index = end_index + 1

        end_index = len(subsets) - 1

        for j in range(start_index, end_index + 1):
            # create a subset with the existing subset and add the new elements to it
            new_set = list(subsets[j])
            new_set.append(sorted_array[i])
            subsets.append(new_set)

    print("Answer is: ", subsets)
    return subsets


assert solve([1, 3, 3]) == [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
assert solve([1, 5, 3, 3]) == [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [
    5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]


"""
Time complexity: O(2^N)
Space complexity: S(2^N)
"""
