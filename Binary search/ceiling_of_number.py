"""
Given an array of numbers sorted in an ascending order, find the ceiling of a given number key. 
The ceiling of the key will be the smallest element in the given 
array greater than or equal to the key.

Write a function to return the index of the ceiling of the key. 
If there isn't any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
"""


def solve(nums: list[int], k: int) -> int:
    """
    To solve this: Binary Search
    We can use a similar approach as discussed in Order-agnostic Binary Search. 
    We will try to search for the key in the given array. If we find the key,
    we return its index as the ceiling. If we can't find the key, the next big 
    number will be pointed out by the index start. Consider Example-2 mentioned above:
    """
    if k > nums[-1]:
        # if its bigger than nums biggest element, return it
        return -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = start + (end-start) // 2

        if nums[middle] < k:
            start = middle + 1

        elif nums[middle] > k:
            end = middle - 1
        else:
            # found k, return it
            return middle

    # If k wasn't found, ceiling is going to be stored on start
    return start


assert solve([4, 6, 10], 6) == 1
assert solve([1, 3, 8, 10, 15], 12) == 4
assert solve([4, 6, 10], 17) == -1
assert solve([4, 6, 10], -1) == 0


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
