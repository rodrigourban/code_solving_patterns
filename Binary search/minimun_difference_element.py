"""
Given an array of numbers sorted in ascending order, find the element in
the array that has the minimum difference with the given key.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""


def solve(nums: list[int], key: int) -> int:
    """
    To solve this: Binary Search
    We will try to search for the key in the given array. 
    If we find the key we will return it as the minimum difference number. 
    If we can't find the key, (at the end of the loop) we can find the differences between 
    the key and the numbers pointed out by indices start and end, as these two numbers will be 
    closest to the key. The number that gives minimum difference will be our required number.
    """
    # base case
    if nums[0] > key:
        # sorted asc, first number is going to be the smallest
        return nums[0]
    if nums[-1] < key:
        # sorted asc, last number is going to be the smallest
        return nums[-1]

    start, end = 0, len(nums) - 1
    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] > key:
            end = middle - 1
        elif nums[middle] < key:
            start = middle + 1
        else:
            print("Answer is: ", nums[middle])
            return nums[middle]

    # at the end, start == end + 1
    # order of subtraction is important! :P

    if (nums[start] - key) < (key - nums[end]):
        print("Answer is: ", nums[start])
        return nums[start]

    print("Answer is: ", nums[end])
    return nums[end]


assert solve([4, 6, 10], key=7) == 6
assert solve([4, 6, 10], key=4) == 4
assert solve([1, 3, 8, 10, 15], key=12) == 10
assert solve([4, 6, 10], key=17) == 10


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
