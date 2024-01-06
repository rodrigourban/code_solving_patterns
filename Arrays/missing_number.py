"""
We are given an array containing n distinct numbers taken from the range 0 to n. 
Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""


def solve(nums: list[int]) -> int:
    """
    To solve this: Cyclic sort
    In this problem, the numbers are ranged from 0 to n, compared to 1 to n in the Cyclic Sort. 
    This will make two changes in our algorithm:
    Each number should be equal to its index, compared to index + 1 in the Cyclic Sort. 
    Therefore => nums[i] == nums[nums[i]]
    Since the array will have n numbers, which means array indices will range from 0 to n-1. 
    Therefore, we will ignore the number n as we cant place it in the array, so => nums[i] < nums.length
    Say we are at index i. If we swap the number at index i to place it at the correct index,
    we can still have the wrong number at index i. This was true in Cyclic Sort too. It didn't 
    cause any problems in Cyclic Sort as over there, we made sure to place one number at its correct place
    in each step, but that wouldn't be enough in this problem as we have one extra number due to the larger
    range. Therefore, we will not move to the next number after the swap until we have a correct number at the index i.
    """
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            # we swap them
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # now they should be in ordered, but missing number is not
    # going to match its index

    for i in range(len(nums)):
        if i != nums[i]:
            print("Answer is: ", i)
            return i
    return -1


assert solve([4, 0, 3, 1]) == 2
assert solve([8, 3, 5, 2, 4, 6, 0, 1]) == 7


"""
Time complexity: O(n) + O(n-1) + O(n) => O(n)
Space complexity: S(1)
"""
