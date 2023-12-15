"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [[], [1], [3], [1,3], [3,3], [1,3,3]]
Example 2:

Input: [1, 5, 3, 3]
Output: [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]
"""


def solve(lst: [int]) -> [[]]:
    """
    To solve this: Breadth First Search (BFS) approach but
    we need to do is handle duplicates by doing extra steps:
    1. Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
    2. Follow the same BFS approach but whenever we are about to process a duplicate 
    (i.e., when the current and the previous numbers are same), instead of adding the current number 
    (which is a duplicate) to all the existing subsets, only add it to the subsets which were created
    in the previous step.
    Ex: [1, 5, 3, 3]  sorted [1, 3, 3, 5]
    a. Start with an empty set: [[]]
    b. Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
    c. Add the second number (3) to all the existing subsets: [[], [1], [3], [1,3]].
    d. The next number (3) is a duplicate. If we add it to all existing subsets we will get:
    [[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]
    We got two duplicate subsets: [3], [1,3]  
    Whereas we only needed the new subsets: [3,3], [1,3,3]  
    To handle this instead of adding (3) to all the existing subsets, we only add it to the new 
    subsets which were created in the previous (3rd) step:
    [[], [1], [3], [1,3], [3,3], [1,3,3]]
    e. Finally, add the forth number (5) to all the existing subsets: 
    [[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]
    """
    # sort list to compare if previous element is same as current
    sorted_lst = sorted(lst)
    combinations = [[]]
    start, end = 0, 0
    for number in sorted_lst:
        to_append = []
        if number in combinations[start]:
            # repeated, only add last combinations
            for i in range(start, end):
                to_append.append([*combinations[i], number])
        else:
            for current in combinations:
                to_append.append([*current, number])
        combinations.extend(to_append)
        start = len(combinations) - len(to_append)
        end = len(combinations)
    return combinations


assert solve([1, 3, 3]) == [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
assert solve([1, 5, 3, 3]) == [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [
    5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]

"""
Time complexity: O(2^N)
Space complexity: O(2^N)
"""
