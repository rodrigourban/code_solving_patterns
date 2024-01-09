"""
Given an array of numbers sorted in ascending order, find the range of a given number key.
The range of the key will be the first and last position of the key in the array.

Write a function to return the range of the key. If the key is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]


I would do the search, once I found the index I would try to increase the index to find the end
of range and decrease index to find the start.
AWe need to find the first and last only.
If I cannot find it, range is [middle, middle]
"""


def binary_search(nums: list[int], key: int, lookForMax: bool = False):
    start, end = 0, len(nums) - 1
    last_index = -1
    while start <= end:
        middle = start + (end - start) // 2

        # base cases
        if nums[middle] < key:
            start = middle + 1
        elif nums[middle] > key:
            end = middle - 1
        else:
            last_index = middle
            # keep looking, right if lookForMax else left
            if lookForMax:
                start = middle + 1
            else:
                end = middle - 1
    return last_index


def solve(nums: list[int], key: int) -> list[int]:
    """
    To solve this: Binary Search
    We will try to search for the key in the given array; if the key is found (i.e. key == arr[middle) we have two options:

    When trying to find the first position of the key, we can update end = middle - 1 to see if the key is present before middle.
    When trying to find the last position of the key, we can update start = middle + 1 to see if the key is present after middle.
    In both cases, we will keep track of the last position where we found the key. These positions will be the required range.
    """
    ans = [-1, -1]  # base case, not found

    # The binary has to know whether to be able look the min or the max index
    # first time is going to find first, and with that we can search last
    first = binary_search(nums, key)
    if first >= 0:
        ans = [first, binary_search(nums, key, True)]

    print("Answer is: ", ans)
    return ans


assert solve([4, 6, 6, 6, 9], key=6) == [1, 3]
assert solve([1, 3, 8, 10, 15], key=10) == [3, 3]
assert solve([1, 3, 8, 10, 15], key=12) == [-1, -1]


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
