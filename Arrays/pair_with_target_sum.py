"""
Given an array of sorted numbers and a target sum, find a pair in 
the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


def solve(nums: [int], target: int) -> []:
    """
    To solve this: Two pointers
    Instead of using a two-pointer or a binary search approach, 
    we can utilize a HashTable to search for the required pair.
    We can iterate through the array one number at a time. 
    Let's say during our iteration we are at number X, so we need to find Y such that
    X+Y==Target”. We will do two things here:
    1. Search for Y (which is equivalent to Target-X) in the HashTable. 
    If it is there, we have found the required pair.
    2. Otherwise, insert X in the HashTable, so that we can search it for the later numbers.
    """

    hash_table = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            print("Answer is: ", [hash_table[target - nums[i]], i])
            return [hash_table[target - nums[i]], i]
        hash_table[nums[i]] = i


assert solve([1, 2, 3, 4, 6], 6) == [1, 3]
assert solve([2, 5, 9, 11], 11) == [0, 2]


"""
Time complexity: O()
Space complexity: S()
"""
