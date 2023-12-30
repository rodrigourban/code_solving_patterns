"""
Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def solve(nums: [int], k: int) -> int:
    """
    To solve this: Sliding Window
    If you observe closely, you will realize that to calculate the sum of a contiguous subarray we can utilize the sum 
    of the previous subarray. For this, consider each subarray as a Sliding Window of size k. To calculate the sum of
    the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate
    the sum of the new position of the sliding window, we need to do two things:

    Subtract the element going out of the sliding window i.e., subtract the first element of the window.
    Add the new element getting included in the sliding window i.e., the element coming right after the end of the window.
    """
    window_sum, window_start = 0, 0
    max_sum = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1

    print(max_sum)
    return max_sum


assert solve([2, 1, 5, 1, 3, 2], 3) == 9
assert solve([2, 1, 5], 3) == 8
assert solve([2, 3, 4, 1, 5], 2) == 7


"""
Time complexity: O(n)
Space complexity: S(1)
"""
