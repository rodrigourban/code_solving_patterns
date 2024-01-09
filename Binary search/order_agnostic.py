"""
Given a sorted array of numbers, find if a given number key is present in the array. 
Though we know that the array is sorted, we don't know if it's sorted in ascending or 
descending order. You should assume that the array can have duplicates.

Write a function to return the index of the key if it is present in the array,
otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2

Input: [2, 6, 7, 10], key = 5
Output: -1

Input [2, 2, 3, 3, 5, 6], key = 3
Output: 3
"""


def solve(nums: list[int], k: int) -> int:
    """
    To solve this: Binary Search
    start = 0;
    end = len(arr) - 1;
    middle = start + (end - start)//2. Strict middle since python has 0 index arrays
    while start <= end
    1. If it is equal we return middle as the required index.
    2. If key is not equal to number at index middle, we have to check two things:
        a.If key < arr[middle], then we can conclude that the key will be smaller than all the 
        numbers after index middle as the array is sorted in the ascending order.
            end = mid - 1.
        b.If key > arr[middle], then we can conclude that the key will be greater than all 
        numbers before index middle as the array is sorted in the ascending order. 
            start = mid + 1.
    If loops ends, key wasn't found, return -1

    When array is sorted in the descending order, step 2 changes to:
    a.If key > arr[middle], then we can conclude that the key will be greater than all
    numbers after index middle as the array is sorted in the descending order. 
        end = mid - 1.
    b.If key < arr[middle], then we can conclude that the key will be smaller than all the
    numbers before index middle as the array is sorted in the descending order. 
        start = mid + 1.
    """
    ans = -1

    # we can check the ordering by checking the first and last elements
    ascending = nums[0] < nums[-1]
    start = 0
    end = len(nums) - 1
    while start <= end:
        # calculate middle
        middle = start + (end - start) // 2

        # check if middle is k
        if nums[middle] == k:
            ans = middle
            break

        # increase or decrease end and start depending of middle and order of nums
        if ascending:
            if nums[middle] < k:
                start = middle + 1
            else:
                end = middle - 1
        else:
            if nums[middle] > k:
                start = middle + 1
            else:
                end = middle - 1

    print("Answer is: ", ans)
    return ans


assert solve([4, 6, 10], 10) == 2
assert solve([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert solve([10, 6, 4], 10) == 0
assert solve([10, 6, 4], 4) == 2
assert solve([2, 6, 7, 10], 5) == -1
assert solve([2, 2, 3, 3, 5, 6], 3) == 2


"""
Time complexity: O(logN)
Space complexity: S(1)
"""
