"""
We are given an unsorted array containing numbers taken from the range 1 to n. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
"""


def solve(nums: list[int]) -> list[int]:
    """
    To solve this: Cyclic Sort
    In this problem, there can be many duplicates whereas in Find the Missing Number
    there were no duplicates and the range was greater than the length of the array.

    However, we will follow a similar approach though as discussed in Find the Missing 
    Number to place the numbers on their correct indices. Once we are done with the cyclic 
    sort we will iterate the array to find all indices that are missing the correct numbers.
    """
    ans: list[int] = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            # we swap them
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # now they should be in ordered, but missing number is not
    # going to match its index

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            ans.append(i + 1)
    print("Answer is: ", ans)
    return ans


assert solve([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7]
assert solve([2, 4, 1, 2]) == [3]
assert solve([2, 3, 2, 1]) == [4]


"""
Time complexity: O(n)
Space complexity: S(1)
"""
