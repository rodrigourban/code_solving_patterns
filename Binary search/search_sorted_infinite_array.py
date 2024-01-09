"""
Given an infinite sorted array (or an array with unknown size), find if a given 
number key is present in the array. Write a function to return the index of the key 
if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be
provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) 
will return the number at index; if the array's size is smaller than the index, it will return Integer.MAX_VALUE.

Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.
Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
Example 3:

Input: [1, 3, 8, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.
Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.

For this problem it's important to know where to start, and where to end
Also know if we are going to allow negatives elements, let's assume we don't.
We know that:
1. Array is ordered, so, we can assume that if the number exists, it has to be
in the lower part of array len of number we are searching + 1
This is slightly slower than checking with index first
2. If we are looking for a negative number, the binary search is going to be inverted
but we don't care since we assume it only has positive numbers

With these things in mind, what we could do is try searching for
start = 0, end = number to find + 1

"""

import math


class ArrayReader:

    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def get(self, index: int) -> int | float:
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def solve(nums: ArrayReader, key: int) -> int:
    """
    To solve this: Binary Search
    The only issue with applying binary search in this problem is that we don't know the bounds of the array. 
    To handle this situation, we will first find the proper bounds of the array where we can perform a binary search.

    An efficient way to find the proper bounds is to start at the beginning of the array with the bound's size 
    as 1 and exponentially increase the bound's size (i.e., double it) until we find the bounds that can have the key.
    """
    start, end = 0, 1
    while nums.get(end) < key:
        newStart = end + 1
        end += (end - start + 1) * 2
        start = newStart

    return binary_search(nums, key, start, end)


def binary_search(nums: ArrayReader, key: int, start: int, end: int):
    print(end)
    while start <= end:
        mid = start + (end - start) // 2
        if nums.get(mid) > key:
            end = mid - 1
        elif nums.get(mid) < key:
            start = mid + 1
        else:
            return mid
    return -1


assert solve(ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20,
             22, 24, 26, 28, 30]), key=16) == 6
assert solve(ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20,
             22, 24, 26, 28, 30]), key=11) == -1
assert solve(ArrayReader([1, 3, 8, 10, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 26, 27, 28]), key=15) == 4
assert solve(ArrayReader([1, 3, 8, 10, 15]), key=200) == -1


"""
Time complexity: O(logN) Searching end index O(logN), binary search O(logN)
    logN + logN = logN
Space complexity: S(1)
"""
