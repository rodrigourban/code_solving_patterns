"""
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9
"""


def solve(lst: list[int]) -> int:
    """
    To solve this: XOR
    Solution with XOR #
    Recall the following two properties of XOR:
    It returns zero if we take XOR of two same numbers.
    It returns the same number if we XOR with zero.
    So we can XOR all the numbers in the input; duplicate numbers will zero out each other 
    and we will be left with the single number.
    """
    x1 = 0
    for i in lst:
        x1 ^= i
    return x1


assert solve([1, 4, 2, 1, 3, 2, 3]) == 4
assert solve([7, 9, 7]) == 9


"""
Time complexity: O(n)
Space complexity: O(1)
"""
