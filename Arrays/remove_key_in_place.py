"""
Given an unsorted array of numbers and a target key, remove all instances of 
key in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""


def solve(nums: [int], key: int) -> int:
    """
    To solve this: Two pointers
    We need to remove the duplicates in-place such that the resultant length
    of the array remains sorted. As the input array is sorted, therefore, 
    one way to do this is to shift the elements left whenever we encounter 
    duplicates. In other words, we will keep one pointer for iterating the 
    array and one pointer for placing the next non-duplicate number. 
    So our algorithm will be to iterate the array and whenever we see a 
    non-duplicate number we move it next to the last non-duplicate number we've seen.
    """

    next_element = 0
    for i in range(0, len(nums)):
        if nums[i] != key:
            nums[next_element] = nums[i]
            next_element += 1

    return next_element


assert solve([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4
assert solve([2, 11, 2, 2, 1], 2) == 2


"""
Time complexity: O(N)
Space complexity: S(1)
"""
